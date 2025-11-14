import pygame
from background import Width, Height, screen
from globals import P1, Asset_paths, Asset_names, Assets, solid_tiles, Level, enemies
from background import screen
from Tile import Tile
import random
from Enemy import Enemy


pygame.init()

tile_size = 128
scale = tile_size/64

###############################################ASSET INITIALIZATION####################################


for i, value in enumerate(Asset_paths):
    name = Asset_names[i]
    image = pygame.image.load(value)
    image = pygame.transform.rotozoom(image,0,scale)
    rect = image.get_rect(center = (tile_size//2,tile_size//2))
    mask = pygame.mask.from_surface(image)
    

    Assets[name] = {
        "image": image,
        "rect" : rect,
        "mask" : mask
    }

i = 0
while len(enemies) == 0:
    for y, row in enumerate(Level):
        for x, cell in enumerate(row):
            if cell == 'floor':
                if random.randint(0,100) > 90:
                    enemy = Enemy(x,y)
                    i += 1
                    enemies[i] = {
                        "x" : x,
                        "y" : y,
                        "version" : enemy
                    }

###############################################ASSET INITIALIZATION####################################

def build_level(level): #builds the level by calling build tile for each element in the level list
    solid_tiles.clear()
    level_width = len(level[0]) * tile_size #sets width of the level
    level_height = len(level) * tile_size #sets height of the level
    offset_x = (Width - level_width) // 2 
    offset_y = (Height - level_height) // 2
    solid_tiles.clear()
    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            build_tile(x + P1.x, y + P1.y, cell, offset_x, offset_y)
            

            
            
def build_tile(x, y, tile_type, offset_x, offset_y):
    

    pos_x = offset_x + x * tile_size
    pos_y = offset_y + y * tile_size
    
    if tile_type in Assets:
        image = Assets[tile_type]["image"]
        tile_rect = image.get_rect(topleft=(pos_x, pos_y))
        if tile_type != "floor":
            newTile = Tile(pos_x, pos_y, tile_rect)
        screen.blit(image, tile_rect)
        for i in enemies:
                if enemies[i]['x'] + P1.x == x and enemies[i]['y'] + P1.y == y:
                   try:
                    enemies[i]['version'].x = enemies[i]['x'] - P1.x
                    enemies[i]['version'].y = enemies[i]['y'] + P1.y
                    screen.blit(enemies[i]['version'].image, tile_rect)
                   except:
                       pass
        try:
            solid_tiles.append(newTile)
        except:
            pass



        

               
    

