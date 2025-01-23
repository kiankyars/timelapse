from moviepy.video.io.VideoFileClip import VideoFileClip

def convert_video_to_mov(input_file: str, output_file: str) -> None:
    """Convert a video to .mov format."""
    video = VideoFileClip(input_file)
    video.write_videofile(output_file, codec="libx264", audio_codec="aac")
    video.close()