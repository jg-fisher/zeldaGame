import pygame

# TILES
DIRT = 0
GRASS = 1
WATER = 2
WALL = 3

# DICTIONARY LINKING TILES TO THEIR COLORS pygame.image.load('pic.png')
TEXTURES = {
    DIRT: pygame.image.load('./textures/dirt.png'),
    GRASS: pygame.image.load('./textures/grass.png'),
    WATER: pygame.image.load('./textures/water.png'),
    WALL: pygame.image.load('./textures/wall.png')
}

# TILES TO BE DISPLAYED
GRID = [
    [WALL, WALL, WALL, GRASS, GRASS, GRASS, GRASS],
    [WALL, GRASS, GRASS, GRASS, DIRT, DIRT, DIRT],
    [WALL, GRASS, GRASS, GRASS, DIRT, DIRT, DIRT],
    [WALL, GRASS, GRASS, GRASS, GRASS, GRASS, DIRT],
    [WALL, WATER, WATER, DIRT, DIRT, DIRT, DIRT],
    [WATER, WATER, WATER, DIRT, WATER, WATER, WATER],
    [DIRT, DIRT, DIRT, DIRT, WATER, WATER, WATER]
]

# GAME DIMENSIONS, CONFIG
TILESIZE = 100 
MAPWIDTH = 7 
MAPHEIGHT = 7 
pygame.init()
DISPLAYSURFACE = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE+125))

# COLORS
WHITE = (200, 200, 200)
BLACK = (0, 0, 0)