import cv2
import os
import sys
import shutil

date = sys.argv[1]

# Define the folder containing images and the output video file
image_folder = f"/Users/Kian/Desktop/timelapses/timelapse_{date}"
output_file = "/Users/Kian/Desktop/timelapses/timelapse.mp4"
20241221
# Get sorted list of image files
images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]

# Ensure there are images to process
if not images:
    raise ValueError("No JPEG images found in the specified folder.")

# Read the first image to get frame dimensions
first_image = cv2.imread(os.path.join(image_folder, images[0]))
height, width, _ = first_image.shape

# Define video writer
fps = 30  # Frames per second
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

# Write images to the video
for image in images:
    img_path = os.path.join(image_folder, image)
    frame = cv2.imread(img_path)
    video.write(frame)

# Release the video writer
video.release()
print(f"Timelapse saved as {output_file}")
shutil.rmtree(image_folder)