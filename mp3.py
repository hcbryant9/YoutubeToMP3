from pytube import YouTube
import os

video_url = input("Enter the URL of the video you want to download:\n>> ")

try:
    
    yt = YouTube(video_url)

    # Check if an audio-only stream is available
    audio_stream = yt.streams.filter(only_audio=True).first()

    if audio_stream:
        # Ask for the destination folder
        print("Enter the destination (leave blank for the current directory)")
        destination = input(">> ") or '.'

        # Download the audio stream
        out_file = audio_stream.download(output_path=destination)

        # Save the file as an MP3
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        # sucess
        print(f"{yt.title} has been successfully downloaded as an MP3.")
    else:
        print("No audio-only stream available for this video.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
