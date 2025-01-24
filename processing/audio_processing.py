from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.io.VideoFileClip import VideoFileClip
import random, os
from utils.config import MUSIC_PATH

def add_audio_to_video(output_file):
    if os.path.exists(MUSIC_PATH):
        # List all songs in the folder
        songs = [song for song in os.listdir(MUSIC_PATH) if song.endswith(('.mp3', '.wav'))]
        if not songs:
            print("No audio files found in the folder.")
            exit(1)
        print("Available songs:")
        for idx, song in enumerate(songs):
            print(f"{idx + 1}: {song}")
        # Prompt user to select a song
        choice = int(input("Enter the number of the song you want to use: ")) - 1
        if choice < 0 or choice >= len(songs):
            print("Invalid choice. Exiting.")
            exit(1)
        selected_song = os.path.join(MUSIC_PATH, songs[choice])
        print(f"Selected song: {selected_song}")

        # Add audio to the video
        video_clip = VideoFileClip(output_file)
        audio_clip = AudioFileClip(selected_song)
        video_duration = video_clip.duration
        audio_duration = audio_clip.duration
        if video_duration > audio_duration:
            raise ValueError("The video duration exceeds the audio file duration.")
        start_time = random.uniform(0, audio_duration - video_duration)
        end_time = start_time + video_duration
        audio_segment = audio_clip.subclip(start_time, end_time)
        video_with_audio = video_clip.set_audio(audio_segment)
        timelapse_with_music = output_file.replace("timelapse_", "")
        video_with_audio.write_videofile(timelapse_with_music, codec="libx264", audio_codec="aac")
        print(f"Timelapse with audio saved as {timelapse_with_music}")
    else:
        print("Music file not found. Timelapse video saved without audio.")
    return timelapse_with_music
