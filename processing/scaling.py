from utils.helpers import extract_time_from_filename
from math import ceil
from datetime import timedelta
from utils.config import INTERVAL, FPS

def scale(images):
    # Get first and last timestamps
    first_time = extract_time_from_filename(images[0])
    last_time = extract_time_from_filename(images[-1])

    # Calculate elapsed time
    elapsed_time = last_time - first_time
    # Total time based on the number of frames and interval
    total_time = timedelta(seconds=INTERVAL * len(images))

    fps = FPS  # Create local variable
    # Calculate the final timelapse duration in seconds
    final_timelapse_duration = len(images) / fps

    # Check if final timelapse duration exceeds 1 minute
    if final_timelapse_duration > 60:
        # scaling factor required to get to one minute
        ratio = final_timelapse_duration / 60
        print(f'''The generated timelapse will be approximately {ceil(final_timelapse_duration)} seconds long, if you want to automatically scale to one minute, press enter''')
        scaling_factor = input("Enter a scaling factor to speed up the video (e.g., 2 for 2x speed-up): ")
        if not scaling_factor:
            scaling_factor = ratio
        if float(scaling_factor) <= 0:
            raise ValueError("Scaling factor must be greater than 0.")
        # Adjust FPS to scale down video duration
        fps = int(fps * float(scaling_factor))
        final_timelapse_duration = len(images) / fps  # Recalculate timelapse duration
        print(f"FPS has been updated to {fps} to accommodate the scaling factor.")
        print(f"New timelapse duration will be approximately {round(final_timelapse_duration)} seconds.")

    return elapsed_time, total_time, fps