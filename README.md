# youtubeDownloader

ou need a module installed named Pytube for downloading YouTube videos.

    pip install pytube==12.1.3 


pytube is a genuine, lightweight, dependency-free Python library (and command-line utility) for downloading YouTube videos.

## Documentation
Detailed documentation about the usage of the library can be found at pytube.io. This is recommended for most cases. If you want to hastily download a single video, the quick start guide below might be what you're looking for.

pytube is a lightweight library written in Python. It has no third-party dependencies and aims to be highly reliable.

urthermore, pytube includes a command-line utility, allowing you to download videos right from the terminal.

### Features
Support for both progressive & DASH streams
Support for downloading the complete playlist
Easily register on_download_progress & on_download_complete callbacks
Command-line interfaced included
Caption track support
Outputs caption tracks to .srt format (SubRip Subtitle)
Ability to capture thumbnail URL
Extensively documented source code
No third-party dependencies

### Sometimes, the PyPI release becomes slightly outdated. To install from the source with pip:


    python -m pip install git+https://github.com/pytube/pytube 



### Using pytube in a python script
To download a video using the library in a script, you'll need to import the YouTube class from the library and pass an argument of the video URL. From there, you can access the streams and download them.

~~~
 from pytube import YouTube
 YouTube('https://youtu.be/2lAe1cqCOXo').streams.first().download()
 yt = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')
 yt.streams
 filter(progressive=True, file_extension='mp4')
 order_by('resolution')
 desc()
 first()
 download()
 ~~~

### Using the command-line interface
Using the CLI is remarkably straightforward as well. To download a video at the highest progressive quality, you can use the following command:

    pytube https://youtube.com/watch?v=2lAe1cqCOXo


### You can also do the same for a playlist:

    pytube https://www.youtube.com/playlist?list=PLS1QulWo1RIaJECMeUT4LFwJ-ghgoSH6n
