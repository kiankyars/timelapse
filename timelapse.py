import cv2
import time
import os
import datetime
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

TIMELAPSE_DIR = os.getenv('TIMELAPSE_DIR', str(Path.home() / 'Desktop' / 'timelapses'))

folder_name = f"timelapse_{datetime.datetime.now().strftime('%Y%m%d')}"
file_path = f'{TIMELAPSE_DIR}/{folder_name}'
os.makedirs(file_path, exist_ok=True)


# Initialize webcam
cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


frame_interval = 10  # Seconds between frames

try:
    while True:
        ret, frame = cap.read()
        if ret:
            timestamp = time.strftime("%H%M%S")
            filename = f"{file_path}/frame_{timestamp}.jpg"
            cv2.imwrite(filename, frame)
            # print(f"Captured {filename}")
        time.sleep(frame_interval)
except KeyboardInterrupt:
    print("Timelapse stopped.")
finally:
    cap.release()
