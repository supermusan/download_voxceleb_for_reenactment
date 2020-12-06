# Download VoxCeleb1&2
This repository is for downloading VoxCeleb1&2

## Preparation
1) Instal requirments:
```
pip install -r requirements.txt
```

2) Load youtube-dl:
```
wget https://yt-dl.org/downloads/latest/youtube-dl -O youtube-dl
chmod a+rx youtube-dl
```

3) Install ffmpeg

```
sudo apt-get install ffmpeg
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


2) Run preprocessing.
```
python crop_vox.py --workers 40 --device_ids 0,1,2,3,4,5,6,7 --format .mp4 --dataset_version 2
python crop_vox.py --workers 40 --device_ids 0,1,2,3,4,5,6,7 --format .mp4 --dataset_version 1 --data_range 10000-11252
```

#### Additional notes

Reference:
https://github.com/AliaksandrSiarohin/video-preprocessing

