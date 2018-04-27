import pygame, sys
from pygame.locals import *
from lib import enemies, heroes, items
from grid import *
import random

# INSTANCES OF GAME OBJECTS
PLAYER = heroes.LINK()
WAND = items.WAND()
GOLD = items.GOLD()
SWORD = items.SWORD()
BEAST = enemies.BEAST()

GAME_ITEMS = [WAND, GOLD, SWORD]

# OTHER CONFIG
INVFONT = pygame.font.SysFont('FreeSansBold.ttf', 20)
HEALTHFONT = pygame.font.SysFont('FreeSansBold.ttf', 40)

# TIMED EVENTS
# pygame.time.set_timer(USEREVENT + 1, 1500)


# IMAGES FOR ANIMATED WALKING
img_path = './sprites/link/link_'
f_path = img_path + 'f' 
b_path = img_path + 'b'
r_path = img_path + 'r'
l_path =  img_path + 'l'

f_images = [f_path+str(f)+'.png' for f in range(7)]
b_images = [b_path+str(b)+'.png' for b in range(7)]
r_images = [r_path+str(r)+'.png' for r in range(7)] 
l_images = [l_path+str(l)+'.png' for l in range(7)]

counter = 0

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
            if (event.key == K_RIGHT) and PLAYER.PLAYER_POS[0] < MAPWIDTH - 1:
                PLAYER.PLAYER_POS[0] += .25
                PLAYER.DIRECTION = 'r'
                
                PLAYER.SPRITE_POS = pygame.image.load(r_images[counter])
                counter = (counter + 1) % len(r_images)
                
            # MOVE LEFT
            elif (event.key == K_LEFT) and PLAYER.PLAYER_POS[0] > 0:
                PLAYER.PLAYER_POS[0] -= .25
                PLAYER.DIRECTION = 'l'

                PLAYER.SPRITE_POS = pygame.image.load(l_images[counter])
                counter = (counter + 1) % len(l_images)

            # MOVE UP
            elif (event.key == K_UP) and PLAYER.PLAYER_POS[1] > 0:
                PLAYER.PLAYER_POS[1] -= .25
                PLAYER.DIRECTION = 'u'
                
                PLAYER.SPRITE_POS = pygame.image.load(b_images[counter])
                counter = (counter + 1) % len(b_images)

            # MOVE DOWN
            elif (event.key == K_DOWN) and PLAYER.PLAYER_POS[1] < MAPHEIGHT - 1:
                PLAYER.PLAYER_POS[1] += .25
                PLAYER.DIRECTION = 'd'

                PLAYER.SPRITE_POS = pygame.image.load(f_images[counter])
                counter = (counter + 1) % len(f_images)

            # PLACING DOWN ITEMS
            elif (event.key == K_SPACE) and WAND  or SWORD in PLAYER.PLAYER_INV:
                PLAYER.PLAYER_INV = []
            
                for item in GAME_ITEMS:
                    if item.PLACED == False:
                        item.PLACED = True

                if PLAYER.DIRECTION == 'd':
                    for item in GAME_ITEMS:
                        item.POS[0] = PLAYER.PLAYER_POS[0] 
                        item.POS[1] = PLAYER.PLAYER_POS[1] - 1
                elif PLAYER.DIRECTION == 'u':
                    for item in GAME_ITEMS:
                        item.POS[0] = PLAYER.PLAYER_POS[0] 
                        item.POS[1] = PLAYER.PLAYER_POS[1] + 1
                elif PLAYER.DIRECTION == 'r':
                    for item in GAME_ITEMS:
                        item.POS[0] = PLAYER.PLAYER_POS[0] - 1
                        item.POS[1] = PLAYER.PLAYER_POS[1] 
                elif PLAYER.DIRECTION == 'l':
                    for item in GAME_ITEMS:
                        item.POS[0] = PLAYER.PLAYER_POS[0] + 1
                        item.POS[1] = PLAYER.PLAYER_POS[1]

#    if event.type == USEREVENT + 1:
#        BEAST.MOVE()

    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            # SURFACE
            DISPLAYSURFACE.blit(TEXTURES[GRID[row][column]], (column*TILESIZE, row*TILESIZE))

            # RENDERING ARMED ITEMS WITH PLAYER SPRITE
            if PLAYER.DIRECTION == 'u':
                # PLAYER ITEM
                if WAND in PLAYER.PLAYER_INV:
                    DISPLAYSURFACE.blit(WAND.IMAGE_ARMED, (PLAYER.PLAYER_POS[0]*TILESIZE,  PLAYER.PLAYER_POS[1]*TILESIZE))
                elif SWORD in PLAYER.PLAYER_INV:
                    DISPLAYSURFACE.blit(SWORD.IMAGE_ARMED, (PLAYER.PLAYER_POS[0]*TILESIZE,  PLAYER.PLAYER_POS[1]*TILESIZE))
                # PLAYER
                DISPLAYSURFACE.blit(PLAYER.SPRITE_POS, (PLAYER.PLAYER_POS[0]*TILESIZE, PLAYER.PLAYER_POS[1]*TILESIZE))
            else:
                # PLAYER
                DISPLAYSURFACE.blit(PLAYER.SPRITE_POS, (PLAYER.PLAYER_POS[0]*TILESIZE, PLAYER.PLAYER_POS[1]*TILESIZE))
                # PLAYER ITEM
                if WAND in PLAYER.PLAYER_INV:
                    DISPLAYSURFACE.blit(WAND.IMAGE_ARMED, (PLAYER.PLAYER_POS[0]*TILESIZE,  PLAYER.PLAYER_POS[1]*TILESIZE))
                elif SWORD in PLAYER.PLAYER_INV:
                    DISPLAYSURFACE.blit(SWORD.IMAGE_ARMED, (PLAYER.PLAYER_POS[0]*TILESIZE,  PLAYER.PLAYER_POS[1]*TILESIZE))



            # BEAST
            DISPLAYSURFACE.blit(BEAST.BEAST, (BEAST.BEAST_POS[0]*TILESIZE, BEAST.BEAST_POS[1]*TILESIZE))
            for tree in trees:
                DISPLAYSURFACE.blit(tree.SPRITE, (tree.X_POS, tree.Y_POS))

            # SWORD
            DISPLAYSURFACE.blit(SWORD.IMAGE, (SWORD.POS[0]*TILESIZE, SWORD.POS[1]*TILESIZE))

            if WAND.PLACED:
                DISPLAYSURFACE.blit(WAND.IMAGE, (WAND.POS[0]*TILESIZE, WAND.POS[1]*TILESIZE))
            if GOLD.PLACED:
                DISPLAYSURFACE.blit(GOLD.IMAGE, (GOLD.POS[0]*TILESIZE, GOLD.POS[1]*TILESIZE))
    
    # PICKUP ITEM CONDITIONS

    for item in GAME_ITEMS:
        if PLAYER.PLAYER_POS == item.POS and item.PLACED:
            PLAYER.PLAYER_INV.append(item)
            item.PLACED = False

    INVENTORY_POSITION = 250 
    for item in PLAYER.PLAYER_INV:
        DISPLAYSURFACE.blit(item.IMAGE, (INVENTORY_POSITION, MAPHEIGHT*TILESIZE+35))
        INVENTORY_POSITION += 10 
        INVENTORY_TEXT = INVFONT.render(item.NAME, True, WHITE, BLACK)
        DISPLAYSURFACE.blit(INVENTORY_TEXT, (INVENTORY_POSITION, MAPHEIGHT*TILESIZE+15))
        INVENTORY_POSITION += 100
    
    # HEALTH BAR
    PLAYER_HEALTH_BAR_TEXT = HEALTHFONT.render('HEALTH:', True, GREEN, BLACK)
    DISPLAYSURFACE.blit(PLAYER_HEALTH_BAR_TEXT, (15, MAPHEIGHT*TILESIZE+15))
    DISPLAYSURFACE.blit(HEALTHFONT.render(str(PLAYER.HEALTH), True, GREEN, BLACK), (150, MAPHEIGHT*TILESIZE+15))

    # MANA BAR
    PLAYER_MANA_BAR_TEXT = HEALTHFONT.render('MANA:', True, BLUE, BLACK)
    DISPLAYSURFACE.blit(PLAYER_MANA_BAR_TEXT, (43.5, MAPHEIGHT*TILESIZE+50))
    DISPLAYSURFACE.blit(HEALTHFONT.render(str(PLAYER.MANA), True, BLUE, BLACK), (150, MAPHEIGHT*TILESIZE+50))

    pygame.display.update()


