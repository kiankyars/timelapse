import os
import shutil
from pathlib import Path
from config import TIMELAPSE_DIR, OUTPUT_DIR, MUSIC_PATH, FPS
from utils.helpers import extract_time_from_filename, get_sorted_images
from processing.image_processing import generate_timelapse, calculate_timelapse_duration
from processing.audio_processing import add_audio_to_video
from processing.video_conversion import convert_video_to_mov

def main(date: str, delete_directory: str):
    image_folder = f"{TIMELAPSE_DIR}/timelapse_{date}"
    images = get_sorted_images(image_folder)
    output_file = f"{OUTPUT_DIR}/timelapse_{date}.mp4"

    # Generate the timelapse
    generate_timelapse(images, image_folder, FPS, output_file)

    # Add music if available
    if os.path.exists(MUSIC_PATH):
        music_file = os.path.join(MUSIC_PATH, random.choice(os.listdir(MUSIC_PATH)))
        output_with_audio = output_file.replace('.mp4', '_with_audio.mp4')
        add_audio_to_video(output_file, music_file, output_with_audio)

        # Convert to .mov
        output_mov = output_with_audio.replace('.mp4', '.mov')
        convert_video_to_mov(output_with_audio, output_mov)

    # Delete the image folder if required
    if delete_directory.lower() == 'y':
        shutil.rmtree(image_folder)

if __name__ == "__main__":
    import sys
    date = sys.argv[1]
    delete_directory = sys.argv[2]
    main(date, delete_directory)