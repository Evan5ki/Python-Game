import pygame
from background import Width, Height
from globals import Asset_paths, Asset_names, Assets, tile_size, scale, Active_level, Loaded_Level
from Tile import Tile
import globals



###############################################ASSET INITIALIZATION####################################


for i, value in enumerate(Asset_paths):
    try:
        name = Asset_names[i]
        image = pygame.transform.rotozoom(pygame.image.load(value),0,scale)
        rect = image.get_rect(center = (tile_size//2,tile_size//2))
    except:
        pass
    

    Assets[name] = {
        "image": image,
        "rect" : rect,
    }
###############################################ASSET INITIALIZATION####################################


###Loads the variable active level which holds a list of lists that contaitn the type of each block in
###that area. This function then passes it to the load tile function with a the x,y position in the list
###the type and the origin calculation
def load_level(): 
    level_width = len(globals.Active_level[0]) * tile_size #sets width of the level
    level_height = len(globals.Active_level) * tile_size #sets height of the level
    origin = (Width//2 - level_width//2, Height//2 - level_height//2)
    for y, row in enumerate(globals.Active_level):
        for x, cell in enumerate(row):
            load_tile(x, y, cell, origin)

###Creates a tile object at a certain X, Y position away from the calculated origin. Then adds this Tile object
###to a list of every other tile in the level
def load_tile(x, y, cell, origin):
    if cell != 'empty':
        tile = Tile(Assets[cell]["image"],  
                    [origin[0] + x * tile_size, origin[1] + y * tile_size], 
                    cell)
        Loaded_Level.append(tile)

###Called every iteration. Updates the position of the tiles in accordance with the speed vector of the player
###Then draws the same level tile at those new tile coords
def update_tiles(xtrans, ytrans):
    for tile in Loaded_Level:
        tile.update(xtrans, ytrans)

###Draws 'em bad bois
def draw_tiles():
    for tile in Loaded_Level:
        tile.draw()