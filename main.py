from pytube import YouTube
from tkinter import *

window = Tk()
window.title("YouTube video downloader")
window.minsize(width=500, height=300)
window.configure(bg='#f5f3f4')

txt = Label(text="YouTube Downloader", font=("Helvetica", 30, "bold"), bg='#f5f3f4', fg='#161a1d', padx=10, pady=20)
txt.pack()


def button_clicked():
    link = input.get()
    yt_obj = YouTube(link)
    yt_obj = yt_obj.streams.get_highest_resolution()
    try:
        txt.config(text="Downloading...\n")
        yt_obj.download()
    except:
        txt.config(text="An error has occurred")
    txt.config(text="Download is completed successfully")


button = Button(text="Click to download", font=("Helvetica", 12, "bold"), bg='#e5383b', fg='#f5f3f4', command=button_clicked)
button.pack()

input = Entry(width=30, fg='#161a1d')
input.pack()

mainloop()
