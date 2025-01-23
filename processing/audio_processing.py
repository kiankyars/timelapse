from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.io.VideoFileClip import VideoFileClip
import random

def add_audio_to_video(video_path: str, music_path: str, output_path: str) -> None:
    """Add audio to a video."""
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(music_path)

    if video_clip.duration > audio_clip.duration:
        raise ValueError("The video duration exceeds the audio file duration.")

    # Trim audio and attach
    start_time = random.uniform(0, audio_clip.duration - video_clip.duration)
    audio_segment = audio_clip.subclip(start_time, start_time + video_clip.duration)
    video_with_audio = video_clip.set_audio(audio_segment)
    video_with_audio.write_videofile(output_path, codec="libx264", audio_codec="aac")