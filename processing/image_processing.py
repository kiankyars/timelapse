import cv2
from datetime import timedelta

def calculate_timelapse_duration(images: list, fps: int) -> float:
    """Calculate the final timelapse duration in seconds."""
    return len(images) / fps

def generate_timelapse(images: list, image_folder: str, fps: int, output_file: str) -> None:
    """Generate a timelapse video from images."""
    # Read dimensions from the first image
    first_image = cv2.imread(f"{image_folder}/{images[0]}")
    height, width, _ = first_image.shape

    # Define video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

    for image in images:
        img_path = f"{image_folder}/{image}"
        frame = cv2.imread(img_path)
        video.write(frame)

    video.release()