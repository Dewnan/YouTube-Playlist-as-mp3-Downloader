import os
from pytube import YouTube
from pytube import Playlist
import re

# Color
RED = "\033[0;31m"
GREEN = "\033[1;32m"
BLUE = "\033[0;34m"
RESET = "\033[0m"

def download_video(video_url, playlist_title):
    try:
        yt = YouTube(video_url)
        stream = yt.streams.filter(only_audio=True).first()
        
        # Replace invalid characters in the title
        title = re.sub(r'[\/:*?"<>|]', '_', stream.title)
        
        output_file = f"{title}.mp3"

        # Check if the file already exists
        if os.path.exists(os.path.join(playlist_title, output_file)):
            print(RED + "[Warning]: " + RESET + f"{output_file} already exists. Skipping...")
            return

        print(GREEN + "[Info]: " + RESET + f"{output_file} Start Downloading..")
        stream.download(output_path=playlist_title, filename=output_file)
        print(GREEN + "[Info]: " + RESET + f"{output_file} Downloaded Successfully...")

    except Exception as e:
        print(RED + "[Error]: " + RESET + f"Error Downloading {video_url}: {e}")


playlist_url = input("Enter URL: ")

playlist = Playlist(playlist_url)
video_urls = playlist.video_urls
playlist_title = playlist.title

# Get playlist title and make folder to save mp3 files
if not os.path.exists(playlist_title):
    os.makedirs(playlist_title)
    print(GREEN + "[Info]: " + RESET + playlist_title + BLUE + " Folder Created." + RESET)

for video_url in video_urls:
    download_video(video_url, playlist_title)

print(GREEN + "Playlist Downloaded Successfully...")
input("Press Enter to Exit...")
