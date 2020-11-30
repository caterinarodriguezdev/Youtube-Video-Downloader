from pytube import YouTube
# I will use this module to create a Graphical User Interface
from tkinter import *

window = Tk()
window.geometry('600x300')

# This function will create an infinite loop that is used to run the application,
# wait for an event to occur and process the event as long as the window is not closed.
window.mainloop()

# "progressive=True" means that it will download the video but only for resolutions 720p and below.
# Instead "adaptive=true" can be used.
# youtubeVideo = YouTube('https://www.youtube.com/watch?v=tPEE9ZwTmy0').streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
# youtubeVideo.download('C:/Users/Caterina/PycharmProjects/youtubeVideos')