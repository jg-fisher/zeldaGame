import pygame, sys
from pygame.locals import *

# TILES
DIRT = 0
GRASS = 1
WATER = 2
WALL = 3

# COLORS
BLACK = (0, 0, 0)
BROWN = (153, 76, 0)
GREEN = (0, 255, 0)
BLUE = (26, 113, 133)

# DICTIONARY LINKING TILES TO THEIR COLORS pygame.image.load('pic.png')
COLORS = {
    DIRT: BROWN,
    GRASS: GREEN,
    WATER: BLUE,
    WALL: BLACK
}

# TILES TO BE DISPLAYED
GRID = [
    [WALL, WALL, WALL, WALL],
    [WALL, GRASS, GRASS, WALL],
    [WALL, GRASS, GRASS, WALL],
    [WALL, GRASS, GRASS, WALL],
    [WALL, WATER, WATER, WATER],
    [WATER, WATER, WATER, DIRT]
]

# GAME DIMENSIONS
TILESIZE = 40
MAPWIDTH = 4
MAPHEIGHT = 6

pygame.init()
DISPLAYSURFACE = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))

GAME_OVER = False

# GAME LOOP
while not GAME_OVER:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        for row in range(MAPHEIGHT):
            for column in range(MAPWIDTH):
                pygame.draw.rect(DISPLAYSURFACE,
                                 COLORS[GRID[row][column]],
                                 (column*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))

        pygame.display.update()


