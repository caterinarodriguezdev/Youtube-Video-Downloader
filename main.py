from pytube import YouTube
# I will use this module to create a Graphical User Interface
from tkinter import StringVar, Label, Entry, Tk, messagebox, Button, Canvas, PhotoImage, font


import os
from pathlib import Path

window = Tk()
window.geometry('700x300')
window.title('Torrapipes Youtube Video Downloader')
window.configure(bg='#2A2F32')

label1 = Label(window, text="Paste a youtube video link here", font=('Adumu', 30), bg='#2A2F32', fg='white')
label1.pack()

linkVideo = StringVar()

# textvariable attribute saves input text into the specified variable, in this case link
linkField = Entry(window, width=60, font='Adumu', textvariable=linkVideo)
linkField.pack(ipady=7)

# Canvas for image
canvas_width = 100
canvas_height = 100

canvas = Canvas(window,
           width=canvas_width,
           height=canvas_height, bd=0, highlightthickness=0, relief='ridge')
canvas.configure(bg='red')
canvas.pack()

img = PhotoImage(file='assets/pyb.pgm')
canvas.create_image(50,50, image=img)

def downloadVideo():
    linkVideoUrl = linkVideo.get()
    # "progressive=True" means that it will download the video but only for resolutions 720p and below.
    # Instead "adaptive=true" can be used.
    youtubeVideo = YouTube(linkVideoUrl).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if os.path.exists(os.path.join(Path.home(),'Descargas')):
        print("using windows spanish")
        pathDownloadFolder = str(os.path.join(Path.home(), 'Descargas'))
    else:
        print("using windows english")
        pathDownloadFolder = str(os.path.join(Path.home(), 'Downloads'))

    youtubeVideo.download(pathDownloadFolder)
    messagebox.showinfo('Video downloaded!', 'Find the video in your downloads folder :)')


buttonFont = font.Font(family='Adumu', size=20)
# command attribute shows which function will be ran when button is clicked
downloadButton = Button(window, text='Download Video', width=20, bg='white', fg='#2A2F32', command=downloadVideo)
downloadButton['font'] = buttonFont
downloadButton.pack()


# This function will create an infinite loop that is used to run the application,
# wait for an event to occur and process the event as long as the window is not closed.
window.mainloop()





