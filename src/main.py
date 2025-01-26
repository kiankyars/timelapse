import os
import sys
import shutil
from pathlib import Path

# Add project root to Python path
sys.path.append(str(Path(__file__).resolve().parent.parent))

# Relative imports from project modules
from utils.config import TIMELAPSE_DIR, MUSIC_PATH
from utils.helpers import get_sorted_images
from processing.image_processing import create_timelapse
from processing.audio_processing import add_audio_to_video
from processing.video_conversion import convert_video_to_mov
from processing.scaling import scale

def main(date: str, delete_directory: str):
    image_folder = f"{TIMELAPSE_DIR}/timelapse_{date}"
    images = get_sorted_images(image_folder)
    elapsed_time, total_time, fps = scale(images)
    output_file = create_timelapse(image_folder, images, elapsed_time, total_time, fps, date)

    # Add music if available
    if not os.path.exists(MUSIC_PATH):
        exit("could not find path to music directory")
    time_lapse_with_music = add_audio_to_video(output_file)
    # unlink current output_file if music was dded so that the real final output file can be assigned
    if os.path.exists(output_file):
        Path.unlink(output_file)
    # Convert to .mov
    output_file = convert_video_to_mov(time_lapse_with_music)

    # Delete the image folder
    if delete_directory == 'y':
        shutil.rmtree(image_folder)
    elif delete_directory == 'n':
        pass
    else:
        exit('incorrect second arguement provided, must be either y or n, (delete or keep)')
    # Delete timelapse in .mp4
    Path.unlink(time_lapse_with_music)

if __name__ == "__main__":
    import sys
    date = sys.argv[1]
    delete_directory = sys.argv[2]
    main(date, delete_directory)