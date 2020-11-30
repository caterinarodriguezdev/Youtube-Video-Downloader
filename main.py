from pytube import YouTube
import os

# "progressive=True" means that it will download the video but only for resolutions 720p and below.
# Instead "adaptive=true" can be used.
youtubeVideo = YouTube('https://www.youtube.com/watch?v=tPEE9ZwTmy0').streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
youtubeVideo.download('C:/Users/Caterina/PycharmProjects/youtubeVideos')