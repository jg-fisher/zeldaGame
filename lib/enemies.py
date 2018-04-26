import pygame.image
from grid import MAPHEIGHT, MAPWIDTH
import random

rand = random.randint

class BEAST:
    BEAST = pygame.image.load('./sprites/beast.png')
    BEAST_POS = [rand(0, MAPWIDTH-1), rand(0, MAPHEIGHT-1)]