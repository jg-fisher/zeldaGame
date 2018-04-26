import pygame.image
from grid import MAPHEIGHT, MAPWIDTH
import random

rand = random.randint

class WAND:
    NAME = 'WAND'
    IMAGE = pygame.image.load('./sprites/wand.png')
    POS = [rand(0, MAPWIDTH-1), rand(0, MAPHEIGHT-1)]
    PLACED = True

class GOLD:
    NAME = 'BITCOIN'
    IMAGE = pygame.image.load('./sprites/gold_coin.png')
    POS = [rand(0, MAPWIDTH-1), rand(0, MAPHEIGHT-1)]
    PLACED = True

