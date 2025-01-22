# Timelapse Creator

A Python script that creates timelapses from a series of JPEG images, with options for timestamps and background music.

## Features
- Captures images at specified intervals
- Creates MP4 videos from captured images
- Adds timestamps to videos
- Optional background music support
- Automatic cleanup of source images

## Requirements
- Python 3.x
- OpenCV
- MoviePy (for audio support)
- python-dotenv

## Installation

1. Install UV if you haven't already:
```bash
pip install uv
# OR
brew install uv
```

2. Create and activate a virtual environment:
```bash
uv venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

3. Install the dependencies:
```bash
uv pip install -r requirements.txt
```

## Usage

1. Capture timelapse images:
```bash
python3 timelapse.py
```

2. Create video from images:
```bash
python3 video.py <date>
```

3. Add timestamps and music (optional):
```bash
python3 add_time.py
```

## Configuration

Create a `.env` file in the project root with:
```bash
# Required
TIMELAPSE_DIR=/path/to/timelapses

# Optional
OUTPUT_DIR=/path/to/output  # Defaults to ~/Desktop
INTERVAL=5                  # Seconds between frames (default: 5)
FPS=60                     # Frames per second in output video (default: 60)
MUSIC_PATH=/path/to/music.mp3  # Optional background music
```

If no TIMELAPSE_DIR is specified, it will default to `~/Desktop/timelapses`

## File Structure
- `timelapse.py`: Captures images at specified intervals
- `video.py`: Converts image sequences to video
- `add_time.py`: Adds timestamps and optional background music to videos

## Output
- Images are saved in `TIMELAPSE_DIR/timelapse_YYYYMMDD/`
- Videos are saved as `timelapse_YYYYMMDD_duration.mp4`
- Timestamped videos are saved as `final_timelapse_YYYYMMDD_duration.mp4`