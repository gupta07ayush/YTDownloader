# Download complete playlist

from pytube import Playlist

playlist_link = "https://youtube.com/playlist?list=PL09avdK_qXyeOItrCF0XekO5ydc8z9-R7"
py_obj = Playlist(playlist_link)

# Get title
print(f'Downloading \n: {py_obj.title}')

# Get all video from playlist in higehest quality
for video in py_obj.videos:
    video.streams.get_highest_resolution().download()