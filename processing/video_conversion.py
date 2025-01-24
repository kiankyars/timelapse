from moviepy.video.io.VideoFileClip import VideoFileClip

def convert_video_to_mov(timelapse_with_music):
    """Convert a video to .mov format."""
    output_file = timelapse_with_music[:-4] + '.mov'
    try:
        video = VideoFileClip(timelapse_with_music)
        video.write_videofile(output_file, codec="libx264", audio_codec="aac")
        print(f"Converted {timelapse_with_music} to {output_file}")
        video.close()
    except Exception as e:
        print(f"An error occurred while converting to .mov: {e}")
    return output_file