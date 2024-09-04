import sys
import os
import pygame

def resource_path(relative_path): #return the path of an embedded file in an exe if it exists, otherwise return its path in the computer
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def playmusic(name): #play music, infinite loop
    pygame.mixer.music.unload()
    pygame.mixer.music.load(resource_path(os.path.join('sound',f'{name}.wav')))
    pygame.mixer.music.play(loops=-1)

def playsound(name): #play a sound once
    pygame.mixer.music.unload()
    pygame.mixer.music.load(resource_path(os.path.join('sound',f'{name}.wav')))
    pygame.mixer.music.play()

def queuemusic(name): #wait for the previous audio to end, then play a new one (for music after sound)
    pygame.mixer.music.queue(resource_path(os.path.join('sound',f'{name}.wav')))