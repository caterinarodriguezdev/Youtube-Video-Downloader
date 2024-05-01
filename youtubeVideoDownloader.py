from pytube import YouTube
# I will use this module to create a Graphical User Interface
from tkinter import StringVar, Label, Entry, Tk, messagebox, Button, Canvas, PhotoImage, font

import os
from pathlib import Path

window = Tk()
window.geometry('700x300')
window.title('Torrapipes Youtube Video Downloader')
window.configure(bg='#2A2F32')

iconPhoto = PhotoImage(file='./assets/icon.png')
window.iconphoto(False, iconPhoto)

label1 = Label(window, text="Paste a youtube video link here", font=('Adumu', 30), bg='#2A2F32', fg='white')
label1.pack()

linkVideo = StringVar()

linkField = Entry(window, width=60, font='Adumu', textvariable=linkVideo)
linkField.pack(ipady=7)

canvas_width = 100
canvas_height = 100

canvas = Canvas(window,
           width=canvas_width,
           height=canvas_height, bd=0, highlightthickness=0, relief='ridge')
canvas.configure(bg='red')
canvas.pack()

img = PhotoImage(file='./assets/pyb.pgm')
canvas.create_image(50,50, image=img)

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


buttonFont = font.Font(family='Adumu', size=20)

downloadButton = Button(window, text='Download Video', width=20, bg='white', fg='#2A2F32', command=downloadVideo)
downloadButton['font'] = buttonFont
downloadButton.pack()

window.mainloop()





