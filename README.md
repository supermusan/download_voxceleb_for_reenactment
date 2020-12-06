# Download VoxCeleb1&2
This repository is for downloading VoxCeleb1&2

## Preparation
1) Instal requirments:
```
pip install -r requirements.txt
```

2) Load youtube-dl:
Linux:
```
wget https://yt-dl.org/downloads/latest/youtube-dl -O youtube-dl
chmod a+rx youtube-dl
```
Window:
```
wget https://github.com/ytdl-org/youtube-dl/releases/download/2020.12.05/youtube-dl.exe
```

3) Install ffmpeg
Linux:
```
sudo apt-get install ffmpeg
```
Windows:
```
wget https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z
# Then, unzip 'ffmpeg-release-full.7z', and move 'ffmpeg-4.3.1-2020-11-19-full_build/bin/ffmpeg.exe' to the run directory.
```

## Download VoxCeleb dataset
1) Load vox-celeb1(vox-celeb2) annotations:

```
wget www.robots.ox.ac.uk/~vgg/data/voxceleb/data/vox1_test_txt.zip
unzip vox1_test_txt.zip

wget www.robots.ox.ac.uk/~vgg/data/voxceleb/data/vox1_dev_txt.zip
unzip vox1_dev_txt.zip
```

```
wget www.robots.ox.ac.uk/~vgg/data/voxceleb/data/vox2_test_txt.zip
unzip vox2_test_txt.zip

wget www.robots.ox.ac.uk/~vgg/data/voxceleb/data/vox2_dev_txt.zip
unzip vox2_dev_txt.zip
```


2) Run scripts.
```
python download_vox.py --workers 4 --dataset_version 2 --remove-intermediate-results
python download_vox.py --workers 4 --dataset_version 1 --data_range 10000-11252 --remove-intermediate-results
```

#### Additional notes

Reference:
https://github.com/AliaksandrSiarohin/video-preprocessing

