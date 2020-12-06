# Video Preprocessing 
This repository provides tools for preprocessing videos for TaiChi, VoxCeleb and UvaNemo dataset used in [paper](https://papers.nips.cc/paper/8935-first-order-motion-model-for-image-animation).

<!---
# Downloading
VoxCeleb with our preprocessing can be download in [.mp4](https://yadi.sk/d/6XkWUoJzjzuwVA) format and in [.png](https://drive.google.com/file/d/1VLhAbzbrexqg-nHq8l1AV8oc-Sq-x0kZ/view?usp=sharing). 

TaiChi can be downloade directly in format [.mp4](https://yadi.sk/d/03C366987mkS1w) or [.png](https://drive.google.com/file/d/10b_OiRxMKRgbrOQHQvM-OEISPWfiM7zY/view?usp=sharing).
-->

## Dowloading videos and cropping according to precomputed bounding boxes
1) Instal requirments:
```
pip install -r requirements.txt
```

2) Load youtube-dl:
```
wget https://yt-dl.org/downloads/latest/youtube-dl -O youtube-dl
chmod a+rx youtube-dl
```

3) Run script to download videos, there are 2 formats that can be used for storing videos one is .mp4 and another is folder with .png images. While .png images occupy significantly more space, the format is loss-less and have better i/o performance when training.


## Preprocessing VoxCeleb dataset

If you need to change cropping strategy for **VoxCeleb** dataset or produce new bounding box annotations folow these steps:

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

2) Load youtube-dl:
```
wget https://yt-dl.org/downloads/latest/youtube-dl -O youtube-dl
chmod a+rx youtube-dl
```

3) Install ffmpeg

```
sudo apt-get install ffmpeg
```

4) Run preprocessing (assuming 8 gpu, and 5 workers per gpu).
```
python crop_vox.py --workers 40 --device_ids 0,1,2,3,4,5,6,7 --format .mp4 --dataset_version 2
python crop_vox.py --workers 40 --device_ids 0,1,2,3,4,5,6,7 --format .mp4 --dataset_version 1 --data_range 10000-11252
```

#### Additional notes

Reference:
https://github.com/AliaksandrSiarohin/video-preprocessing

