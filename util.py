import numpy as np
import imageio

from multiprocessing import Pool
from itertools import cycle
from tqdm import tqdm
import os

def scheduler(data_list, fn, args):
    device_ids = args.device_ids.split(",")
    pool = Pool(processes=args.workers)
    args_list = cycle([args])

    for chunks_data in tqdm(pool.imap_unordered(fn, zip(data_list, cycle(device_ids), args_list))):
        for data in chunks_data:
            print (line.format(**data), file=f)
            f.flush()


def save(path, frames, format):
    if format == '.mp4':
        imageio.mimsave(path, frames)
    elif format == '.png':
        if os.path.exists(path):
            print ("Warning: skiping video %s" % os.path.basename(path))
            return
        else:
            os.makedirs(path)
        for j, frame in enumerate(frames):
            imageio.imsave(os.path.join(path, str(j).zfill(7) + '.png'), frames[j]) 
    else:
        print ("Unknown format %s" % format)
        exit()
