import pygame.image
from grid import MAPHEIGHT, MAPWIDTH
import random

rand = random.randint

class WAND:
    WAND = pygame.image.load('./sprites/wand.png')
    WAND_POS = [rand(0, MAPWIDTH-1), rand(0, MAPHEIGHT-1)]
    PLACED = True