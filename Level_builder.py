import pygame
from background import Width, Height, screen
from movement import player
pygame.init()

tile_size = 100

###############################################ASSET INITIALIZATION####################################
Asset_paths = [
    'Assets/Level Assets/PNG/Tiles/tile_282.png', 'Assets/Level Assets/PNG/Tiles/tile_309.png', 'Assets/Level Assets/PNG/Tiles/tile_96.png',
    'Assets/Level Assets/PNG/Tiles/tile_280.png', 'Assets/Level Assets/PNG/Tiles/tile_307.png', 'Assets/Level Assets/PNG/Tiles/tile_281.png',
    'Assets/Level Assets/PNG/Tiles/tile_308.png', 'Assets/Level Assets/PNG/Tiles/tile_313.png', 'Assets/Level Assets/PNG/Tiles/tile_285.png',
    'Assets/Level Assets/PNG/Tiles/tile_312.png', 'Assets/Level Assets/PNG/Tiles/tile_286.png'
    ]
Asset_names = [
    'wall_side', 'wall_up', 'floor','uleft_corner', 'lleft_corner', 'uright_corner', 'lright_corner', 'cwall_l', 
    'cwall_r', 'cwall_u', 'cwall_d'
]
Assets = {}
scale = tile_size/64

for i, value in enumerate(Asset_paths):
    Assets[Asset_names[i]] = pygame.image.load(value)

for i, value in enumerate(Asset_names):
    Assets[Asset_names[i]] = pygame.transform.rotozoom(Assets[Asset_names[i]],0,scale)


###############################################ASSET INITIALIZATION####################################

def build_level(level): #builds the level by calling build tile for each element in the level list
    level_width = len(level[0]) * tile_size
    level_height = len(level) * tile_size

    offset_x = (Width - level_width) // 2
    offset_y = (Height - level_height) // 2

    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            build_tile(x + player["x"], y + player["y"], cell, offset_x, offset_y)


def build_tile(x, y, tile_type, offset_x, offset_y): #Builds each tile in the correct location
    # compute pixel position
    pos_x = offset_x + x * tile_size
    pos_y = offset_y + y * tile_size
    
    if tile_type in Assets:
        screen.blit(Assets[tile_type], (pos_x, pos_y))
    else:
        pass
    