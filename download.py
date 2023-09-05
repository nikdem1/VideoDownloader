#!/usr/bin/env python
from os import system

system("title Youtube/Pornhub Video Downloader by Guka")

import youtube_dl
def main():
    print("[YT PH] Youtube/Pornhub Video Downloader by Guka") #please dont delete this
    print("[!] Auto Loop Script, Use Ctrl + C to Stop")
    directory = input("[*] Folder Directory for Saving : ")
    while True:
        url = input("[*] Videos Url : ")
        dire = directory+'/handpicked/%(title)s.%(ext)s'
        ydl_opts = {
            'format': 'best',
            'outtmpl': dire,
            'nooverwrites': True,
            'no_warnings': False,
            'ignoreerrors': True,
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])


if __name__ == '__main__':
    main()
