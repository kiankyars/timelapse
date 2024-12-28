# Timelapse Creator

A Python script that creates timelapses from a series of JPEG images.

## Requirements
- OpenCV (cv2)
- Python 3.x
- Python-dotenv
- opencv-python

## Usage

```
python3 timelapse.py
python3 video.py <date>
```

## Configuration

Create a `.env` file in the project root with:

```
TIMELAPSE_DIR=/path/to/timelapses
```

If no path is specified, it will default to `~/Desktop/timelapses`
