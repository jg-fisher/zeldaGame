import pygame
import random

# TILES
DIRT = 0
GRASS = 1
WATER = 2
WALL = 3
TREE_0 = 4
TREE_1 = 5
TREE_2 = 6

class Tree:
    def __init__(self):
        self.SPRITE = pygame.transform.scale(pygame.image.load('./textures/trees/tree.png'), (125, 125))
        self.X_POS = random.randint(100, 600)
        self.Y_POS = random.randint(100, 700)

class TEMPLE:
    def __init__(self):
        self.SPRITE = pygame.transform.scale(pygame.image.load('./sprites/temple.png'), (250, 250))
        self.X_POS = .5
        self.Y_POS = .2 

num_trees = 15
trees = [Tree() for x in range (num_trees)]

# DICTIONARY LINKING TILES TO THEIR COLORS pygame.image.load('pic.png')
TEXTURES = {
    DIRT: pygame.image.load('./textures/dirt.png'),
    GRASS: pygame.image.load('./textures/grass.png'),
    WATER: pygame.image.load('./textures/water.png'),
    WALL: pygame.image.load('./textures/wall.png'),
    TREE_0: pygame.image.load('./textures/trees/tree.png'),
    TREE_1: pygame.image.load('./textures/trees/tree_1.png'),
}

# TILES TO BE DISPLAYED
GRID = [
    [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, WATER, WATER, WATER],
    [GRASS, GRASS, GRASS, GRASS, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, GRASS, GRASS, WATER, WATER, WATER, WATER, WATER],
    [GRASS, GRASS, GRASS, GRASS, GRASS, GRASS, DIRT, DIRT, DIRT, DIRT, GRASS, GRASS, GRASS, GRASS, GRASS, WATER, WATER, WATER, GRASS, GRASS],
    [GRASS, GRASS, GRASS, GRASS, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, GRASS, GRASS, GRASS, WATER, WATER, WATER, WATER, GRASS, GRASS, GRASS],
    [GRASS, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, GRASS, GRASS, GRASS, WATER, WATER, GRASS, GRASS, GRASS, GRASS, GRASS],
    [DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, WATER, WATER, WATER, WATER, GRASS, GRASS, GRASS],
    [DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, WATER, WATER, WATER, WATER, WATER, WATER, WATER, GRASS, GRASS],
    [GRASS, GRASS, GRASS, GRASS, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, WATER, WATER, WATER, WATER, WATER, WATER, GRASS, GRASS, GRASS],
    [GRASS, GRASS, GRASS, GRASS, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, WATER, WATER, WATER, WATER, WATER, WATER, WATER, GRASS, GRASS],
    [GRASS, GRASS, GRASS, GRASS, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, DIRT, WATER, WATER, WATER, WATER, WATER, WATER, WATER, WATER, GRASS]
]

# GAME DIMENSIONS, CONFIG
TILESIZE = 75 
MAPWIDTH = 20
MAPHEIGHT = 10 
pygame.init()
pygame.display.set_caption('LINKS ADVENTURE')
# MAPHEIGHT + 125 for inventory
DISPLAYSURFACE = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))

# COLORS
WHITE = (200, 200, 200)
BLACK = (0, 0, 0)
BLUE = (30, 144, 255)
GREEN = (60, 179, 113)