import pygame.image
from grid import *

class LINK:
    def __init__(self):
        self.SPRITE_POS = pygame.image.load('./sprites/link/link_f6.png')
        self.PLAYER_POS = [0, 0]
        self.PLAYER_INV = []
        self.WEAPON = False
        self.HEALTH = 100
        self.MANA = 200
        self.DIRECTION = False
        self.TRANSFORM = False
        self.WOLF = pygame.image.load('./sprites/wolf/wolf_f0.png')
    
    def TRANSFORMING(self):
        self.TRANSFORM = not self.TRANSFORM

class MIDNA:
    def __init__(self):
        self.SPRITE_POS = pygame.transform.scale(pygame.image.load('./sprites/midna.png'), (50, 75))
        self.APPEARED = False

class ORB:
    def __init__(self, X, Y, DIRECTION):
        self.IMAGE = pygame.transform.scale(pygame.image.load('./sprites/orb.png'), (25, 25))
        self.POS = [X, Y]
        self.DIRECTION = DIRECTION