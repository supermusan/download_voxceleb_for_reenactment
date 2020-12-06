import numpy as np
import pandas as pd
import imageio
import os
import subprocess
import warnings
import glob
import time
from argparse import ArgumentParser
from multiprocessing import Pool
from itertools import cycle
from tqdm import tqdm
import os
warnings.filterwarnings("ignore")

DEVNULL = open(os.devnull, 'wb')

def download(video_id, args):
    video_path = os.path.join(args.video_folder, video_id + ".mp4")
    subprocess.call([args.youtube, '-f', "''best/mp4''", '--write-auto-sub', '--write-sub',
                     '--sub-lang', 'en', '--skip-unavailable-fragments',
                     "https://www.youtube.com/watch?v=" + video_id, "--output",
                     video_path], stdout=DEVNULL, stderr=DEVNULL)
    return video_path


def split_in_utterance(person_id, video_id, args):
    video_path = os.path.join(args.video_folder, video_id + ".mp4")

    if not os.path.exists(video_path):
        print("No video file %s found, probably broken link" % video_id)
        return []

    utterance_folder = os.path.join(args.annotations_folder, person_id, video_id)
    utterance_files = sorted(os.listdir(utterance_folder))
    utterances = [pd.read_csv(os.path.join(utterance_folder, f), sep='\t', skiprows=6) for f in
                  utterance_files]

    chunk_names = []

    for i, utterance in enumerate(utterances):
        first_frame, last_frame = utterance['FRAME '].iloc[0], utterance['FRAME '].iloc[-1]

        first_frame = round(first_frame / float(REF_FPS), 3)
        last_frame = round(last_frame / float(REF_FPS), 3)

        chunk_name = os.path.join(args.chunk_folder,
                                  video_id + '#' + utterance_files[i] + '#' + str(first_frame) + '-' + str(
                                      last_frame) + '.mp4')

        chunk_names.append(chunk_name)

        subprocess.call(['ffmpeg', '-y', '-i', video_path, '-qscale:v',
                         '5', '-r', '25', '-threads', '1', '-ss', str(first_frame), '-to', str(last_frame),
                         '-strict', '-2', '-deinterlace', chunk_name],
                        stdout=DEVNULL, stderr=DEVNULL)
    return chunk_names


def run(params):
    person_id, args = params
    video_folder = os.path.join(args.annotations_folder, person_id)

    chunks_data = []
    for video_id in os.listdir(video_folder):
        intermediate_files = []
        try:
            if args.download:
                video_path = download(video_id, args)
                intermediate_files.append(video_path)

            if args.split_in_utterance:
                chunk_names = split_in_utterance(person_id, video_id, args)
                # intermediate_files += chunk_names

            if args.remove_intermediate_results:
                for file in intermediate_files:
                    if os.path.exists(file):
                        os.remove(file)
        except Exception as e:
            print (e)
    return chunks_data


if __name__ == "__main__":
    parser = ArgumentParser()

    parser.add_argument("--dataset_version", default=2, type=int, choices=[1, 2], help='Version of Vox celeb dataset 1 or 2')

    parser.add_argument("--annotations_folder", default='txt', help='Path to utterance annotations')

    parser.add_argument("--video_folder", default='videos', help='Path to intermediate videos')
    parser.add_argument("--chunk_folder", default='chunks', help="Path to folder with video chunks")

    parser.add_argument("--youtube", default='./youtube-dl', help='Command for launching youtube-dl')
    parser.add_argument("--workers", default=1, type=int, help='Number of parallel workers')

    parser.add_argument("--data_range", default=(0, 10000), type=lambda x: tuple(map(int, x.split('-'))), help="Range of ids for processing")


    parser.add_argument("--no-download", dest="download", action="store_false", help="Do not download videos")
    parser.add_argument("--no-split-in-utterance", dest="split_in_utterance", action="store_false",
                        help="Do not split videos in chunks")

    parser.add_argument("--remove-intermediate-results", dest="remove_intermediate_results", action="store_true",
                        help="Remove intermediate videos")

    parser.set_defaults(download=True)
    parser.set_defaults(split_in_utterance=True)
    parser.set_defaults(remove_intermediate_results=False)

    args = parser.parse_args()
    print(args)

    if not os.path.exists(args.video_folder):
        os.makedirs(args.video_folder)
    if not os.path.exists(args.chunk_folder):
        os.makedirs(args.chunk_folder)


    ids = set(os.listdir(args.annotations_folder))
    ids_range = {'id' + str(num).zfill(5) for num in range(args.data_range[0], args.data_range[1])}
    ids = sorted(list(ids.intersection(ids_range)))

    pool = Pool(processes=args.workers)
    args_list = cycle([args])

    for chunks_data in tqdm(pool.imap_unordered(run, zip(ids, args_list))):
        None

