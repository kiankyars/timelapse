import cv2
import os
from datetime import datetime, timedelta
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.io.VideoFileClip import VideoFileClip

from moviepy.editor.ImageSequenceClip import ImageSequenceClip
from pathlib import Path
from dotenv import load_dotenv

def extract_time_from_filename(filename):
    """Extracts the time from the filename in HHMMSS format."""
    match = re.search(r"frame_(\d{6})\.jpg", filename)
    if match:
        time_str = match.group(1)
        return f"{time_str[:2]}:{time_str[2:4]}:{time_str[4:]}"
    return None

def create_timelapse_with_timestamps(frame_folder, output_video, audio_file=None):
    """
    Create a timelapse video with timestamps overlayed from frame filenames.

    Args:
        frame_folder (str): Path to the folder containing frames.
        output_video (str): Path for the output video file.
        audio_file (str): Path to an audio file to add to the video (optional).
    """
    # Get sorted list of frame filenames
    frame_files = sorted(
        [f for f in os.listdir(frame_folder) if f.endswith(".jpg")],
        key=lambda x: int(re.search(r"(\d+)", x).group(1))
    )

    # Read the first frame to get video dimensions
    first_frame_path = os.path.join(frame_folder, frame_files[0])
    first_frame = cv2.imread(first_frame_path)
    height, width, _ = first_frame.shape

    # Define font properties for timestamp
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1.5
    font_color = (255, 255, 255)  # White
    thickness = 2
    timestamp_position = (50, height - 50)

    processed_frames = []

    for frame_file in frame_files:
        frame_path = os.path.join(frame_folder, frame_file)
        frame = cv2.imread(frame_path)

        # Extract timestamp from filename
        timestamp = extract_time_from_filename(frame_file)
        if not timestamp:
            print(f"Skipping file {frame_file}: Unable to extract timestamp.")
            continue

        # Overlay timestamp on frame
        cv2.putText(frame, timestamp, timestamp_position, font, font_scale, font_color, thickness, cv2.LINE_AA)
        processed_frames.append(frame)

    # Save frames as video
    output_fps = 30
    video_filename = "temp_video.mp4"
    height, width, _ = processed_frames[0].shape

    out = cv2.VideoWriter(video_filename, cv2.VideoWriter_fourcc(*"mp4v"), output_fps, (width, height))
    for frame in processed_frames:
        out.write(frame)
    out.release()

    # Add audio if provided
    if audio_file:
        video = ImageSequenceClip([cv2.cvtColor(f, cv2.COLOR_BGR2RGB) for f in processed_frames], fps=output_fps)
        audio = AudioFileClip(audio_file)
        audio = audio.set_duration(video.duration)
        final_video = video.set_audio(audio)
        final_video.write_videofile(output_video, codec="libx264")
        os.remove(video_filename)
    else:
        os.rename(video_filename, output_video)

if __name__ == "__main__":
    frame_folder = "path/to/frames"  # Replace with your frames folder path
    output_video = "output_timelapse.mp4"  # Replace with desired output video path
    audio_file = "path/to/audio.mp3"  # Optional: replace with your audio file path or None

    create_timelapse_with_timestamps(frame_folder, output_video, audio_file)
