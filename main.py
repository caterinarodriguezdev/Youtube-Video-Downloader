from pytube import YouTube
# I will use this module to create a Graphical User Interface
from tkinter import *
import os
from pathlib import Path

window = Tk()
window.geometry('600x300')
window.title('Torrapipes Youtube Video Downloader')

label1 = Label(window, text="Paste Youtube Video Link Here", font=('bold', 20))
label1.pack()

linkVideo = StringVar()

# textvariable attribute saves input text into the specified variable, in this case link
linkField = Entry(window, width=60, textvariable=linkVideo)
linkField.pack()

def downloadVideo():
    linkVideoUrl = linkVideo.get()
    youtubeVideo = YouTube(linkVideoUrl).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    # if not os.path.exists('\youtubeVideos'):
    #     os.makedirs('\youtubeVideos')
    pathDownloadFolder = str(os.path.join(Path.home(),'Descargas'))
    youtubeVideo.download(pathDownloadFolder)


# command attribute shows which function will be ran when button is clicked
downloadButton = Button(window, text='Download Video', width=20, bg='red', fg='white', command=downloadVideo)
downloadButton.pack()


# This function will create an infinite loop that is used to run the application,
# wait for an event to occur and process the event as long as the window is not closed.
window.mainloop()

# "progressive=True" means that it will download the video but only for resolutions 720p and below.
# Instead "adaptive=true" can be used.



