import pygame, sys
from pygame.locals import *
from lib import enemies, heroes, items
from grid import *
import random
from key_events import KeyEvents
import math

# INSTANCES OF GAME OBJECTS
PLAYER = heroes.LINK()
key_events = KeyEvents(PLAYER)

#MIDNA = heroes.MIDNA()

WAND = items.WAND()
GOLD = items.GOLD()
SWORD = items.SWORD()
SHIELD = items.SHIELD()
BOW = items.BOW()

GANON = enemies.GANON()
PORTAL = enemies.PORTAL()
TEMPLE = TEMPLE()

# GROUPINGS OF RELATED GAME OBJECTS
GAME_ITEMS = [WAND, SWORD, SHIELD]
GAME_WEAPONS = [WAND, SWORD]
BEAST_LIST = []

# OTHER CONFIG
INVFONT = pygame.font.SysFont('FreeSansBold.ttf', 20)
HEALTHFONT = pygame.font.SysFont('FreeSansBold.ttf', 40)

# TIMED EVENTS
# GANON MOVEMENT
pygame.time.set_timer(USEREVENT, 400)
# SPAWN BEAST
pygame.time.set_timer(USEREVENT + 1, 15000)
# INCREMENT BEAST PORTAL FRAMES
pygame.time.set_timer(USEREVENT + 2, 400)
# BEAST MOVEMENT
pygame.time.set_timer(USEREVENT + 3, 10)

portal_path = './textures/portal/portal_'
portal_images = [portal_path + str(p) + '.png' for p in range(1, 7)]

GAME_OVER = False
# GAME LOOP
while not GAME_OVER:

    # IS GANON VULNERABLE 
    if len(BEAST_LIST) == 0:
        GANON.VULNERABLE = True

    for event in pygame.event.get():

        keys = pygame.key.get_pressed()
        key_events.global_events()

        if event.type == QUIT:
            key_events.quit()

            # MOVE RIGHT
        if (keys[K_RIGHT]) and PLAYER.PLAYER_POS[0] < MAPWIDTH - 1:
           key_events.key_right() 

        # MOVE LEFT
        if (keys[K_LEFT]) and PLAYER.PLAYER_POS[0] > 0:
           key_events.key_left() 

        # MOVE UP
        if (keys[K_UP]) and PLAYER.PLAYER_POS[1] > 0:
            key_events.key_up()

        # MOVE DOWN
        if (keys[K_DOWN]) and PLAYER.PLAYER_POS[1] < MAPHEIGHT - 1:
            key_events.key_down()

        # PLACING DOWN ITEMS
        if (keys[K_SPACE]):
            key_events.key_space()

        if (keys[K_t]):
            key_events.key_w()
            
        # GANON W/PORTAL MOVEMENT
        if (event.type == USEREVENT):
          if PORTAL.FRAME < 5:
              PORTAL.FRAME += 1
          else:
              x = random.randint(1, 9)
              y = random.randint(1, 9)
              PORTAL.POS = [x, y]
              GANON.GANON_POS = [x, y]
              PORTAL.FRAME = 1
        
        # BEAST OBJECT GENERATOR 
        if (event.type == USEREVENT + 1):
            NEW_BEAST = enemies.BEAST()
            NEW_BEAST.PORTAL = enemies.PORTAL()
            BEAST_LIST.append(NEW_BEAST)

       # BEAST W/PORTAL GENERATOR 
        if (event.type == USEREVENT + 2):
            for beast in BEAST_LIST:
                if beast.PORTAL_APPEAR and beast.PORTAL.FRAME < 5:
                    beast.PORTAL.FRAME += 1
                elif not beast.SUMMONED:
                    beast.POS = [beast.PORTAL.POS[0], beast.PORTAL.POS[1]]
                    beast.PORTAL_APPEAR = False
                    beast.APPEAR = True
                    beast.SUMMONED = True
        
        if (event.type == USEREVENT + 3):
            for beast in BEAST_LIST:
                if beast.APPEAR:
                    for coordinate in range(len(beast.POS)):
                        if PLAYER.PLAYER_POS[coordinate] > beast.POS[coordinate]:
                            beast.POS[coordinate] += .01
                        else:
                            beast.POS[coordinate] -= .01

    # PICKUP ITEM CONDITIONS
    for item in GAME_ITEMS:
        print(PLAYER.PLAYER_POS)
        print(item.POS)
        if math.ceil(PLAYER.PLAYER_POS[0]) == item.POS[0] and math.ceil(PLAYER.PLAYER_POS[1]) == item.POS[1] and item.PLACED:
            PLAYER.PLAYER_INV.append(item)
            item.PLACED = False
            # IF PICKED UP WEAPON ARM IT
            if item in GAME_WEAPONS:
                PLAYER.WEAPON = item

    # RENDER GAME GRID
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            DISPLAYSURFACE.blit(TEXTURES[GRID[row][column]], (column*TILESIZE, row*TILESIZE))


    # RENDER PLAYER
    if PLAYER.TRANSFORM:
        DISPLAYSURFACE.blit(PLAYER.WOLF, (PLAYER.PLAYER_POS[0]*TILESIZE, PLAYER.PLAYER_POS[1]*TILESIZE))
    else:
        DISPLAYSURFACE.blit(PLAYER.SPRITE_POS, (PLAYER.PLAYER_POS[0]*TILESIZE, PLAYER.PLAYER_POS[1]*TILESIZE))

    # RENDER TEMPLE
    DISPLAYSURFACE.blit(TEMPLE.SPRITE, (TEMPLE.X_POS*TILESIZE, TEMPLE.Y_POS*TILESIZE))

    #MIDNA.APPEARED = True
    ## RENDER MIDNA
    #if MIDNA.APPEARED:
    #    if PLAYER.TRANSFORM:
    #        DISPLAYSURFACE.blit(MIDNA.SPRITE_POS, (PLAYER.PLAYER_POS[0]*TILESIZE + 20, PLAYER.PLAYER_POS[1] * TILESIZE + 35))
    #    else:
    #        DISPLAYSURFACE.blit(MIDNA.SPRITE_POS, (TEMPLE.X_POS*TILESIZE, TEMPLE.Y_POS*TILESIZE))

    # RENDERING ARMED ITEMS WITH PLAYER SPRITE
    if PLAYER.WEAPON:
        DISPLAYSURFACE.blit(PLAYER.WEAPON.IMAGE_ARMED, (PLAYER.PLAYER_POS[0]*TILESIZE, PLAYER.PLAYER_POS[1]*TILESIZE))

    # RENDER PORTAL
    DISPLAYSURFACE.blit(pygame.image.load(portal_images[PORTAL.FRAME]), (GANON.GANON_POS[0]*TILESIZE, GANON.GANON_POS[1]*TILESIZE))

    # RENDER GANON
    DISPLAYSURFACE.blit(GANON.GANON, (GANON.GANON_POS[0]*TILESIZE, GANON.GANON_POS[1]*TILESIZE))

    # RENDER BEASTS AND BEASTS
    for beast in BEAST_LIST:
        # RENDER PORTALS
        if beast.PORTAL_APPEAR:
            DISPLAYSURFACE.blit(pygame.image.load(portal_images[beast.PORTAL.FRAME]), (beast.PORTAL.POS[0]*TILESIZE, beast.PORTAL.POS[1]*TILESIZE))
        # RENDER BEASTS
        if beast.APPEAR:
            DISPLAYSURFACE.blit(beast.BEAST, (beast.POS[0]*TILESIZE, beast.POS[1]*TILESIZE))
        if beast.POS == PLAYER.PLAYER_POS:
            PLAYER.HEALTH -= 10
    
    print(PLAYER.HEALTH)
        
    if PLAYER.HEALTH == 0:
        GAME_OVER = True

    # RENDER ITEMS
    for item in GAME_ITEMS:
        if item.PLACED == True:
            DISPLAYSURFACE.blit(pygame.transform.scale(item.IMAGE, (75, 75)), (item.POS[0]*TILESIZE, item.POS[1]*TILESIZE))

#    """
#    RENDERING PLAYER INVENTORY (have a render inventory function, that calls a filter function to filter out items)
#    """
#    INVENTORY_POSITION = 250
#    for item in PLAYER.PLAYER_INV:
#        DISPLAYSURFACE.blit(item.IMAGE, (INVENTORY_POSITION, MAPHEIGHT*TILESIZE+35))
#        INVENTORY_POSITION += 10 
#        INVENTORY_TEXT = INVFONT.render(item.NAME, True, WHITE, BLACK)
#        DISPLAYSURFACE.blit(INVENTORY_TEXT, (INVENTORY_POSITION, MAPHEIGHT*TILESIZE+15))
#        INVENTORY_POSITION += 100
#
#    """
#    RENDERING PLAYER STATS 
#    """
#    
#    # HEALTH BAR
#    PLAYER_HEALTH_BAR_TEXT = HEALTHFONT.render('HEALTH:', True, GREEN, BLACK)
#    DISPLAYSURFACE.blit(PLAYER_HEALTH_BAR_TEXT, (15, MAPHEIGHT*TILESIZE+15))
#    DISPLAYSURFACE.blit(HEALTHFONT.render(str(PLAYER.HEALTH), True, GREEN, BLACK), (150, MAPHEIGHT*TILESIZE+15))
#
#    # MANA BAR
#    PLAYER_MANA_BAR_TEXT = HEALTHFONT.render('MANA:', True, BLUE, BLACK)
#    DISPLAYSURFACE.blit(PLAYER_MANA_BAR_TEXT, (43.5, MAPHEIGHT*TILESIZE+50))
#    DISPLAYSURFACE.blit(HEALTHFONT.render(str(PLAYER.MANA), True, BLUE, BLACK), (150, MAPHEIGHT*TILESIZE+50))
#
#    # RENDER TREES
#    for tree in sorted(trees, key=lambda t: t.Y_POS):
#        DISPLAYSURFACE.blit(tree.SPRITE, (tree.X_POS, tree.Y_POS))
#
    pygame.display.update()


# END OF GAME LOOP

