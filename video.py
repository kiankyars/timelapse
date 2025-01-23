import cv2
import os
import sys
import shutil
import random
from pathlib import Path
from dotenv import load_dotenv
from datetime import datetime, timedelta
# from moviepy.editor import VideoFileClip, AudioFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.io.VideoFileClip import VideoFileClip
import random


# Load environment variables
load_dotenv()

date = sys.argv[1]

TIMELAPSE_DIR = os.getenv('TIMELAPSE_DIR', str(Path.home() / 'Desktop' / 'timelapses'))
OUTPUT_DIR = os.getenv('OUTPUT_DIR', str(Path.home() / 'Desktop'))
FPS = int(os.getenv('FPS', 60))
INTERVAL = int(os.getenv('INTERVAL', 5))
MUSIC_PATH = os.getenv('MUSIC_PATH')


# Define the folder containing images and the output video file
image_folder = f"{TIMELAPSE_DIR}/timelapse_{date}"

# Get sorted list of image files
images = [img for img in os.listdir(image_folder) if img.endswith('.jpg')]
images.sort()

# Remove '.DS_Store' if present
if '.DS_Store' in images:
    images.remove('.DS_Store')

# Ensure there are images to process
if not images:
    raise ValueError("No JPEG images found in the specified folder.")

# Extract times from filenames
def extract_time_from_filename(filename):
    time_str = filename.split('_')[1].split('.')[0]  # Extract HHMMSS from filename
    return datetime.strptime(time_str, '%H%M%S')

# Get first and last timestamps
first_time = extract_time_from_filename(images[0])
last_time = extract_time_from_filename(images[-1])

# Calculate elapsed time
elapsed_time = last_time - first_time
# Total time based on the number of frames and interval
total_time = timedelta(seconds=INTERVAL * len(images))

# Read the first image to get frame dimensions
first_image = cv2.imread(os.path.join(image_folder, images[0]))
height, width, _ = first_image.shape

# Define video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_file = f"{OUTPUT_DIR}/timelapse_{date}_{elapsed_time}_{total_time}.mp4"
video = cv2.VideoWriter(output_file, fourcc, FPS, (width, height))

# Write images to the video with timestamps
for image in images:
    img_path = os.path.join(image_folder, image)
    frame = cv2.imread(img_path)

    # Extract and format timestamp
    timestamp = extract_time_from_filename(image).strftime('%H:%M')
    # Add timestamp to the frame
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    color = (255, 255, 255)  # White text
    thickness = 2
    text_size = cv2.getTextSize(timestamp, font, font_scale, thickness)[0]
    org = (width - text_size[0] - 10, 30)  # Top-right corner
    cv2.putText(frame, timestamp, org, font, font_scale, color, thickness, cv2.LINE_AA)
    video.write(frame)

# Release the video writer
video.release()
if os.path.exists(MUSIC_PATH):
    # List all songs in the folder
    songs = [song for song in os.listdir(MUSIC_PATH) if song.endswith(('.mp3', '.wav'))]
    if not songs:
        print("No audio files found in the folder.")
        exit(1)
    print("Available songs:")
    for idx, song in enumerate(songs):
        print(f"{idx + 1}: {song}")
    # Prompt user to select a song
    choice = int(input("Enter the number of the song you want to use: ")) - 1
    if choice < 0 or choice >= len(songs):
        print("Invalid choice. Exiting.")
        exit(1)
    selected_song = os.path.join(MUSIC_PATH, songs[choice])
    print(f"Selected song: {selected_song}")

    # Add audio to the video
    video_clip = VideoFileClip(output_file)
    audio_clip = AudioFileClip(selected_song)
    video_duration = video_clip.duration
    audio_duration = audio_clip.duration
    if video_duration > audio_duration:
        raise ValueError("The video duration exceeds the audio file duration.")
    start_time = random.uniform(0, audio_duration - video_duration)
    end_time = start_time + video_duration
    audio_segment = audio_clip.subclip(start_time, end_time)
    video_with_audio = video_clip.set_audio(audio_segment)
    final_output_file = output_file.replace("timelapse_", "")
    video_with_audio.write_videofile(final_output_file, codec="libx264", audio_codec="aac")
    print(f"Timelapse with audio saved as {final_output_file}")
else:
    print("Music file not found. Timelapse video saved without audio.")


# Delete the image folder
shutil.rmtree(image_folder)
# Delete timelapse w/o music 
Path.unlink(output_file)