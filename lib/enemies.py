import pygame.image
from grid import MAPHEIGHT, MAPWIDTH
import random

rand = random.randint

class GANON:
    def __init__(self):
        self.GANON = pygame.image.load('./sprites/ganon.png')
        self.GANON_POS = [rand(0, MAPWIDTH-1), rand(0, MAPHEIGHT-1)]
        self.VULNERABLE = False

class BEAST:
    def __init__(self):
        self.BEAST = pygame.image.load('./sprites/beast.png')
        self.PORTAL = False
        self.PORTAL_APPEAR = True
        self.APPEAR = False
        self.POS = []
        self.SUMMONED = False

class PORTAL:
    def __init__(self):
        self.PORTAL = pygame.image.load('./textures/portal/portal_1.png')
        self.POS = [rand(0, MAPWIDTH-1), rand(0, MAPHEIGHT-1)]
        self.FRAME = 0