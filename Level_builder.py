import pygame
from background import Width, Height, screen
from globals import P1, Asset_paths, Asset_names, Assets, tile_size, scale, built_tiles
from Tile import Tile




###############################################ASSET INITIALIZATION####################################


for i, value in enumerate(Asset_paths):
    try:
        name = Asset_names[i]
        image = pygame.transform.rotozoom(pygame.image.load(value),0,scale)
        rect = image.get_rect(center = (tile_size//2,tile_size//2))
        mask = pygame.mask.from_surface(image)
    except:
        pass
    

    Assets[name] = {
        "image": image,
        "rect" : rect,
        "mask" : mask
    }





###############################################ASSET INITIALIZATION####################################

def build_level(level, xtrans, ytrans): #builds the level by calling build tile for each element in the level list
    built_tiles.clear()
    level_width = len(level[0]) * tile_size #sets width of the level
    level_height = len(level) * tile_size #sets height of the level
    origin = (Width//2 - level_width//2, Height//2 - level_height//2)
    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            build_tile(x, y, cell, origin, xtrans, ytrans)

    return built_tiles
                

            
            
def build_tile(x, y, tile_type, origin, xtrans, ytrans):
    if tile_type != 'empty':
        tile = Tile(Assets[tile_type]["image"],  
                    [origin[0] + x * tile_size + xtrans, origin[1] + y * tile_size + ytrans], 
                    tile_type)
        #print(f"xtran: {xtrans}")
        built_tiles.append(tile)
        

def let_there_be_level():
    for tiles in built_tiles:
        screen.blit(tiles.surface, tiles.coords)
        #tiles.draw()
        

               
    

