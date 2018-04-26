import pygame.image
from grid import MAPHEIGHT, MAPWIDTH
import random

rand = random.randint

class BEAST:
    def __init__(self):
        self.BEAST = pygame.image.load('./sprites/beast.png')
        self.BEAST_POS = [rand(0, MAPWIDTH-1), rand(0, MAPHEIGHT-1)]
    
    def MOVE(self):
        self.BEAST_POS[0] += rand(-1, 1)
        self.BEAST_POS[1] += rand(-1, 1)