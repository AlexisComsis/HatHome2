from tools import *
import pygame
#HEEY
from entity import *
from tools import *
from player import *
from background import *

pygame.mixer.pre_init(44100, -16, 2, 2048)  #bug soundp
pygame.init()

window = pygame.display.set_mode((tools.w0, tools.h0), pygame.FULLSCREEN)

from textbox import *
from load import *
# Set icon
pygame.display.set_icon(icon)

# Set title
pygame.display.set_caption("HatHome")

# Set Music
pygame.mixer.music.load("Assets\Music\music.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(4)

# Tick Init
clock = pygame.time.Clock()

# Create player
home = Player(750, 400, spriteplayer[0], 100, 50, spriteplayer)
background = Background(5, background, 0, 0)
