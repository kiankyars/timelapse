from pathlib import Path
import os

# Load environment variables
from dotenv import load_dotenv

load_dotenv()

# Directory paths
TIMELAPSE_DIR = os.getenv('TIMELAPSE_DIR', str(Path.home() / 'Desktop' / 'timelapses'))
OUTPUT_DIR = os.getenv('OUTPUT_DIR', str(Path.home() / 'Desktop'))
MUSIC_PATH = os.getenv('MUSIC_PATH')

# Default settings
FPS = int(os.getenv('FPS', 60))
INTERVAL = int(os.getenv('INTERVAL', 5))