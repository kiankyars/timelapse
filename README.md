# Timelapse Creator

A Python script that creates timelapses from a series of JPEG images.

## Requirements
- Python 3.x


## Installation

1. Install UV if you haven't already:

```
pip install uv OR brew install uv
```

2. Create and activate a virtual environment:

```
uv venv
source .venv/bin/activate # On Windows use: .venv\Scripts\activate

```

3. Install the dependencies:

```
uv pip install -r requirements.txt
```

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
