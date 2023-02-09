from pytube import YouTube
from colorama import Style

red = '\033[38;2;255;0;0m'
white = '\033[38;2;255;255;255m'

print(f'''{red}
█▄█ {white}█▀█ █░█ {red}▀█▀ {white}█░█ █▄▄ █▀▀
{red}░█░ {white}█▄█ █▄█ {red}░█░ {white}█▄█ █▄█ ██▄
{white}█▀▄ █▀█ █░█░█ █▄░█ █░░ █▀█ ▄▀█ █▀▄ █▀▀ █▀█
█▄▀ █▄█ ▀▄▀▄▀ █░▀█ █▄▄ █▄█ █▀█ █▄▀ ██▄ █▀▄          

''')

def Download(link):
    yt_obj = YouTube(link)
    yt_obj = yt_obj.streams.get_highest_resolution()
    try:
        print("Downloading...\n")
        yt_obj.download()
    except:
        print(f"{red}An error has occurred")
    print("Download is completed successfully")


link = input("Enter the Youtube video URL: ")
Download(link)
