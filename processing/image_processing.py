import cv2
import os

from utils.config import OUTPUT_DIR
from utils.helpers import extract_time_from_filename

def create_timelapse(image_folder, images, elapsed_time, total_time, fps, date):
    # Read the first image to get frame dimensions
    first_image = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, _ = first_image.shape

    # Define video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output_file = f"{OUTPUT_DIR}/timelapse_{date}_{elapsed_time}_{total_time}.mp4"
    video = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

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
    return output_file