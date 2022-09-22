from datetime import datetime
from os import startfile
import os
from pyautogui import click
from keyboard import press
from keyboard import press_and_release
from keyboard import write
from time import sleep
import webbrowser as web
from pyautogui import click, hotkey
import pyperclip
from pytube import YouTube
def YouTubeAuto(command):

    query = str(command)

    if 'pause' in query:

        press('space bar')

    elif 'resume' in query:

        press('space bar')

    elif 'full screen' in query:

        press('f')

    elif 'film screen' in query:

        press('t')

    elif 'skip' in query:

        press('l')

    elif 'back' in query:

        press('j')

    elif 'increase' in query:

        press_and_release('up')

    elif 'decrease' in query:

        press_and_release('down')

    elif 'previous' in query:

        press_and_release('SHIFT + p')

    elif 'next' in query:

        press_and_release('SHIFT + n')
    
    elif 'mute' in query:

        press('m')

    elif 'unmute' in query:

        press('m')

    elif 'close window' in query:

        press_and_release('Alt + esc')

    elif "download" in query:
            try:
                press_and_release('Ctrl + l')
                hotkey('ctrl','c')
                value = pyperclip.paste()
                link = str(value)
                url = YouTube(link)
                print(url)
                video = url.streams.get_highest_resolution()
                video.download()
                print("video downloaded")
            except Exception as e:
                    print(e)

    else:
        pass