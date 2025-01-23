from datetime import datetime
import os

def extract_time_from_filename(filename: str) -> datetime:
    """Extract timestamp from a filename."""
    time_str = filename.split('_')[1].split('.')[0]
    return datetime.strptime(time_str, '%H%M%S')

def get_sorted_images(image_folder: str) -> list:
    """Get a sorted list of image filenames in the given folder."""
    images = [img for img in os.listdir(image_folder) if img.endswith('.jpg')]
    images.sort()
    if '.DS_Store' in images:
        images.remove('.DS_Store')
    if not images:
        raise ValueError("No JPEG images found in the specified folder.")
    return images