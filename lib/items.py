import pygame.image
from grid import MAPHEIGHT, MAPWIDTH
import random

rand = random.randint

def UPDATE_ARMED_SPRITE(GAME_ITEMS):
    for item in GAME_ITEMS:
        item.POS[0] = PLAYER.PLAYER_POS[0] 
        item.POS[1] = PLAYER.PLAYER_POS[1] - 1

class SWORD:
    def __init__(self):
        self.NAME = 'SWORD'
        self.IMAGE = pygame.image.load('./sprites/sword.png')
        self.IMAGE_ARMED = pygame.transform.scale(self.IMAGE, (35, 35))
        self.POS = [rand(0, MAPWIDTH-1), rand(0, MAPHEIGHT-1)]
        self.PLACED = True

class WAND:
    def __init__(self):
        self.NAME = 'WAND'
        self.IMAGE = pygame.image.load('./sprites/wand.png')
        self.IMAGE_ARMED = pygame.transform.scale(self.IMAGE, (35, 35))
        self.POS = [rand(0, MAPWIDTH-1), rand(0, MAPHEIGHT-1)]
        self.PLACED = True

class GOLD:
    NAME = 'BITCOIN'
    IMAGE = pygame.image.load('./sprites/gold_coin.png')
    POS = [rand(0, MAPWIDTH-1), rand(0, MAPHEIGHT-1)]
    PLACED = True

