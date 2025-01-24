# 🎥 Timelapse Creator

Create stunning timelapses with ease, complete with timestamps and custom music.

## ✨ Features

- 📸 Capture images at configurable intervals
- 🎬 Generate high-quality video timelapses
- ⏰ Automatic timestamp overlay
- 🎵 Optional background music integration
- 🧹 Flexible image source management

## 🛠 Prerequisites

- Python 3.8+
- OpenCV
- MoviePy
- python-dotenv

## 🚀 Quick Start

### Installation

## Install UV (recommended)
```bash
# If on mac
brew install uv
# Otherwise
pip install uv

# Create virtual environment
uv venv
source .venv/bin/activate

# Install dependencies
uv pip install -r requirements.txt
```

### Configuration

Create a `.env` file:

```bash
# Timelapse Settings
TIMELAPSE_DIR=/path/to/timelapses
OUTPUT_DIR=/path/to/output
INTERVAL=5       # Seconds between frames
FPS=60           # Output video frames per second
MUSIC_PATH=/path/to/music/directory
```

### Usage

```bash
# Create timelapse
python main.py <date> <delete_images_flag>

# Examples
python main.py 20240123 y   # Create timelapse, delete source images
python main.py 20240123 n   # Create timelapse, keep source images
```

## 📂 Project Structure

```
timelapse_project/
│
├── src/
│   ├── main.py             # main function
│   └── timelapse.py        # Main capture script
│
├── processing/
│   ├── image_processing.py # Image to video conversion
│   ├── audio_processing.py # Music integration
│   └── video_conversion.py # Video format handling
│
├── utils/
│   ├── config.py           # Configuration management
│   └── helpers.py          # Utility functions
│
├── requirements.txt
└── README.md
```

## 🔧 Customization

- Adjust capture intervals in `.env`
- Select background music interactively
- Configure video parameters flexibly

## 📝 License

MIT

## 🤝 Contributing

Contributions welcome! Please read the contributing guidelines before getting started.