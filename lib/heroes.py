import pygame.image
from grid import *

class LINK:
    def __init__(self):
        self.SPRITE_POS = pygame.image.load('./sprites/link/link_f6.png')
        self.PLAYER_POS = [0, 0]
        self.PLAYER_INV = []
        self.HEALTH = 100
        self.MANA = 200
        
        self.DIRECTION = ''

    def UPDATE_SPRITE(self, DIRECTION):
        """
        For directional sprite animations.

        'f', 'b', 'r', 'l'
        """
        self.direction = DIRECTION

        """
        if self.direction == 'f':

        elif self.direction == 'b':
        
        if self.direction == 'l':

        elif self.direction == 'r':
        """