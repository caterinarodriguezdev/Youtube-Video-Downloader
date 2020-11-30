
from pytube import YouTube
# I will use this module to create a Graphical User Interface
from tkinter import StringVar
from tkinter import Label
from tkinter import Entry
from tkinter import Tk
from tkinter import messagebox
from tkinter import Button

import os
from pathlib import Path

window = Tk()
window.geometry('600x300')
window.title('Torrapipes Youtube Video Downloader')

label1 = Label(window, text="Paste youtube video link here", font=('Montserrat', 20))
label1.pack()

linkVideo = StringVar()

# textvariable attribute saves input text into the specified variable, in this case link
linkField = Entry(window, width=60, textvariable=linkVideo)
linkField.pack()

def downloadVideo():
    linkVideoUrl = linkVideo.get()
    youtubeVideo = YouTube(linkVideoUrl).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if os.path.exists(os.path.join(Path.home(),'Descargas')):
        print("using windows spanish")
        pathDownloadFolder = str(os.path.join(Path.home(), 'Descargas'))
    else:
        print("using windows english")
        pathDownloadFolder = str(os.path.join(Path.home(), 'Downloads'))

    youtubeVideo.download(pathDownloadFolder)
    messagebox.showinfo('Video downloaded!', 'Find the video in your downloads folder :)')



# command attribute shows which function will be ran when button is clicked
downloadButton = Button(window, text='Download Video', width=20, bg='#26a8a8', fg='white', command=downloadVideo)
downloadButton.pack()


# This function will create an infinite loop that is used to run the application,
# wait for an event to occur and process the event as long as the window is not closed.
window.mainloop()

# "progressive=True" means that it will download the video but only for resolutions 720p and below.
# Instead "adaptive=true" can be used.



