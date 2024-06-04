#this file contains all the basic variables for my game
from os import path
import pygame
import sys

#sound and image directories
img_dir = path.join(path.dirname(__file__), 'img')
snd_dir = path.join(path.dirname(__file__), 'snd')



# pygame variables
WIDTH = 820
HEIGHT = 580
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)