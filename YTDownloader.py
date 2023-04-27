# Y and T are capital in YouTube
from pytube import YouTube

youtube_video_link = "https://youtube.com/shorts/pVMldM3PF-o?feature=share"

# make object of YouTube()
youtube_obj= YouTube(youtube_video_link)
# Now this variable youtube_obj contains all the information of the video of the given link

# Get the title of the video
print(youtube_obj.title)  # Method 1

link_title = youtube_obj.title 
print(link_title) # Method 2


# Get the url of the thumbnail image of video
print(youtube_obj.thumbnail_url)
# If you copy paste the output url in the browser, You will get the thumbnail image.


# Get the all video streaming quality in the variable streaming_quality
streaming_quality = youtube_obj.streams.all()   # All format
# Get only Audio list:
# streaming_quality = youtube_obj.streams.filter(only_audio = True)   # All format


# Collect all the data of streaming quality into the list
streaming_quality_list = list(enumerate(streaming_quality))
# using enumerate to get index number of every quality

for i in streaming_quality_list:
    print(i)
    # print all data one by one.
    
print()

# Take the index input of from streaming quality list. Which quality video you want to download.
resolution = int(input("Enter the index of quality: "))
streaming_quality[resolution].download()
print("Downloading....")
print("Downloaded.")


