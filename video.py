import cv2
import os
import sys
import shutil
from pathlib import Path
from dotenv import load_dotenv
from datetime import datetime, timedelta

# Load environment variables
load_dotenv()

date = sys.argv[1]

TIMELAPSE_DIR = os.getenv('TIMELAPSE_DIR', str(Path.home() / 'Desktop' / 'timelapses'))
OUTPUT_DIR = os.getenv('OUTPUT_DIR', str(Path.home() / 'Desktop'))
FPS = int(os.getenv('FPS', 60))
INTERVAL = int(os.getenv('INTERVAL', 5))

# Define the folder containing images and the output video file
image_folder = f"{TIMELAPSE_DIR}/timelapse_{date}"


# Get sorted list of image files
images = [img for img in os.listdir(image_folder)]
images.sort()
# remove '.DS_Store'
if '.DS_Store' in images:
  images.remove('.DS_Store')
# Extract times from first and last images
first_time = images[0].split('_')[1].split('.')[0]
last_time = images[-1].split('_')[1].split('.')[0]
# Convert string times to datetime objects and get elapsed time in seconds
elapsed_time = datetime.strptime(last_time, '%H%M%S') - datetime.strptime(first_time, '%H%M%S')
# total time in seconds
total_time = INTERVAL * len(images)
# total formatted time
total_time = timedelta(seconds=total_time)

# Ensure there are images to process
if not images:
    raise ValueError("No JPEG images found in the specified folder.")

# Read the first image to get frame dimensions
first_image = cv2.imread(os.path.join(image_folder, images[0]))
height, width, _ = first_image.shape

# Define video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_file = f"{OUTPUT_DIR}/timelapse_{date}_{elapsed_time}_{total_time}.mp4"
video = cv2.VideoWriter(output_file, fourcc, FPS, (width, height))

# Write images to the video
for image in images:
    img_path = os.path.join(image_folder, image)
    frame = cv2.imread(img_path)
    video.write(frame)

# Release the video writer
video.release()
print(f"Timelapse saved as {output_file}")
# delete the image folder
shutil.rmtree(image_folder)