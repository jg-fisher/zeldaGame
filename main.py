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
SHIELD = items.SHIELD()
GANON = enemies.GANON()
PORTAL = enemies.PORTAL()

GAME_ITEMS = [WAND, GOLD, SWORD, SHIELD]
GAME_WEAPONS = [WAND, SWORD]

# OTHER CONFIG
INVFONT = pygame.font.SysFont('FreeSansBold.ttf', 20)
HEALTHFONT = pygame.font.SysFont('FreeSansBold.ttf', 40)

# TIMED EVENTS

# GANON MOVEMENT
pygame.time.set_timer(USEREVENT, 250)

# SPAWN BEAST
pygame.time.set_timer(USEREVENT + 1, 5000)


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

beast_list = []
portal_list = []
portal_path = './textures/portal/portal_'
portal_images = [portal_path + str(p) + '.png' for p in range(1, 7)]

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
            elif (event.key == K_SPACE):
                if PLAYER.WEAPON:
                    PLAYER.PLAYER_INV.remove(PLAYER.WEAPON)
                    PLAYER.WEAPON.PLACED = True

                    # DROP WEAPON LOCATION
                    if PLAYER.DIRECTION == 'd':
                            PLAYER.WEAPON.POS[0] = PLAYER.PLAYER_POS[0]
                            PLAYER.WEAPON.POS[1] = PLAYER.PLAYER_POS[1] - 1
                    elif PLAYER.DIRECTION == 'u':
                            PLAYER.WEAPON.POS[0] = PLAYER.PLAYER_POS[0]
                            PLAYER.WEAPON.POS[1] = PLAYER.PLAYER_POS[1] + 1
                    elif PLAYER.DIRECTION == 'r':
                            PLAYER.WEAPON.POS[0] = PLAYER.PLAYER_POS[0] - 1
                            PLAYER.WEAPON.POS[1] = PLAYER.PLAYER_POS[1]
                    elif PLAYER.DIRECTION == 'l':
                            PLAYER.WEAPON.POS[0] = PLAYER.PLAYER_POS[0] + 1
                            PLAYER.WEAPON.POS[1] = PLAYER.PLAYER_POS[1]
                
                PLAYER.WEAPON = False
            
        elif (event.type == USEREVENT):
            if PORTAL.FRAME < 5:
                PORTAL.FRAME += 1
            else:
                x = random.randint(1, 9)
                y = random.randint(1, 9)
                PORTAL.POS = [x, y]
                GANON.GANON_POS = [x, y]
                PORTAL.FRAME = 1
        
        elif (event.type == USEREVENT + 1):
            NEW_BEAST = enemies.BEAST()
            NEW_BEAST.PORTAL = enemies.PORTAL()
            beast_list.append(NEW_BEAST)

            for beast in beast_list:
                if beast.PORTAL.FRAME < 5:
                    beast.PORTAL_APPEAR = True
                    beast.PORTAL.FRAME += 1
                else:
                    beast.APPEAR = True
                    beast.PORTAL_APPEAR = False
                
    # PICKUP ITEM CONDITIONS
    for item in GAME_ITEMS:
        if PLAYER.PLAYER_POS == item.POS and item.PLACED:
            PLAYER.PLAYER_INV.append(item)
            item.PLACED = False
            # IF PICKED UP WEAPON ARM IT
            if item in GAME_WEAPONS:
                PLAYER.WEAPON = item

    # RENDER GAME GRID
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            DISPLAYSURFACE.blit(TEXTURES[GRID[row][column]], (column*TILESIZE, row*TILESIZE))

    # sort trees by y coordinate low ---> high before rendering 
    # RENDER TREES
    for tree in sorted(trees, key=lambda t: t.Y_POS):
        DISPLAYSURFACE.blit(tree.SPRITE, (tree.X_POS, tree.Y_POS))

    # RENDER PLAYER
    DISPLAYSURFACE.blit(PLAYER.SPRITE_POS, (PLAYER.PLAYER_POS[0]*TILESIZE, PLAYER.PLAYER_POS[1]*TILESIZE))

    # RENDERING ARMED ITEMS WITH PLAYER SPRITE
    if PLAYER.WEAPON:
        DISPLAYSURFACE.blit(PLAYER.WEAPON.IMAGE_ARMED, (PLAYER.PLAYER_POS[0]*TILESIZE, PLAYER.PLAYER_POS[1]*TILESIZE))

    # RENDER PORTAL
    print(PORTAL.FRAME)
    DISPLAYSURFACE.blit(pygame.image.load(portal_images[PORTAL.FRAME]), (GANON.GANON_POS[0]*TILESIZE, GANON.GANON_POS[1]*TILESIZE))

    # RENDER GANON
    DISPLAYSURFACE.blit(GANON.GANON, (GANON.GANON_POS[0]*TILESIZE, GANON.GANON_POS[1]*TILESIZE))

    # RENDER BEASTS AND BEASTS
    for beast in beast_list:
        # RENDER PORTALS
        if beast.PORTAL_APPEAR:
            DISPLAYSURFACE.blit(pygame.image.load(portal_images[beast.PORTAL.FRAME]), (beast.PORTAL.POS[0]*TILESIZE, beast.PORTAL.POS[1]*TILESIZE))
            print(beast.PORTAL.POS[0])
        # RENDER BEASTS
        if beast.APPEAR:
            DISPLAYSURFACE.blit(beast.BEAST, (beast.PORTAL.POS[0]*TILESIZE, beast.PORTAL.POS[1]*TILESIZE))
            print(beast.PORTAL.POS[0])

    # RENDER ITEMS
    for item in GAME_ITEMS:
            if item.PLACED == True:
                DISPLAYSURFACE.blit(item.IMAGE, (item.POS[0]*TILESIZE, item.POS[1]*TILESIZE))

    """
    RENDERING PLAYER INVENTORY (have a render inventory function, that calls a filter function to filter out items)
    """
    INVENTORY_POSITION = 250
    for item in PLAYER.PLAYER_INV:
        DISPLAYSURFACE.blit(item.IMAGE, (INVENTORY_POSITION, MAPHEIGHT*TILESIZE+35))
        INVENTORY_POSITION += 10 
        INVENTORY_TEXT = INVFONT.render(item.NAME, True, WHITE, BLACK)
        DISPLAYSURFACE.blit(INVENTORY_TEXT, (INVENTORY_POSITION, MAPHEIGHT*TILESIZE+15))
        INVENTORY_POSITION += 100

    """
    RENDERING PLAYER STATS 
    """
    
    # HEALTH BAR
    PLAYER_HEALTH_BAR_TEXT = HEALTHFONT.render('HEALTH:', True, GREEN, BLACK)
    DISPLAYSURFACE.blit(PLAYER_HEALTH_BAR_TEXT, (15, MAPHEIGHT*TILESIZE+15))
    DISPLAYSURFACE.blit(HEALTHFONT.render(str(PLAYER.HEALTH), True, GREEN, BLACK), (150, MAPHEIGHT*TILESIZE+15))

    # MANA BAR
    PLAYER_MANA_BAR_TEXT = HEALTHFONT.render('MANA:', True, BLUE, BLACK)
    DISPLAYSURFACE.blit(PLAYER_MANA_BAR_TEXT, (43.5, MAPHEIGHT*TILESIZE+50))
    DISPLAYSURFACE.blit(HEALTHFONT.render(str(PLAYER.MANA), True, BLUE, BLACK), (150, MAPHEIGHT*TILESIZE+50))

    pygame.display.update()

# END OF GAME LOOP

