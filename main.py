import pygame, sys
from pygame.locals import *
import random

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

# GAME DIMENSIONS
TILESIZE = 100 
MAPWIDTH = 7 
MAPHEIGHT = 7 

pygame.init()

DISPLAYSURFACE = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))

# PLAYER .convertalpha() ?
PLAYER = pygame.image.load('./sprites/link.png')
PLAYER_POS = [0, 0]

# ENEMIES
BEAST = pygame.image.load('./sprites/beast.png')
BEAST_POS = [random.randint(0, MAPWIDTH-1), random.randint(0, MAPHEIGHT-1)]

print(BEAST_POS)

GAME_OVER = False

# GAME LOOP
while not GAME_OVER:

    for event in pygame.event.get():
        print(event)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif (event.type == pygame.locals.KEYDOWN):
            # MOVE RIGHT
            if (event.key == K_RIGHT) and PLAYER_POS[0] < MAPWIDTH - 1:
                PLAYER_POS[0] += 1
            # MOVE LEFT
            elif (event.key == K_LEFT) and PLAYER_POS[0] > 0:
                PLAYER_POS[0] -=1
            # MOVE UP
            elif (event.key == K_UP) and PLAYER_POS[1] > 0:
                PLAYER_POS[1] -= 1
            elif (event.key == K_DOWN) and PLAYER_POS[1] < MAPHEIGHT - 1:
                PLAYER_POS[1] += 1

    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            DISPLAYSURFACE.blit(TEXTURES[GRID[row][column]], (column*TILESIZE, row*TILESIZE))
            DISPLAYSURFACE.blit(PLAYER, (PLAYER_POS[0]*TILESIZE, PLAYER_POS[1]*TILESIZE))
            DISPLAYSURFACE.blit(BEAST, (BEAST_POS[0]*TILESIZE, BEAST_POS[1]*TILESIZE))

    pygame.display.update()


