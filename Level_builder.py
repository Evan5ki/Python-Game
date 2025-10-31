import pygame
from background import Width, Height, screen
from movement import player
pygame.init()

tile_size = 64

###############################################ASSET INITIALIZATION####################################
walls = 'Assets/Level Assets/PNG/Tiles/tile_282.png'
wallu = 'Assets/Level Assets/PNG/Tiles/tile_309.png'
floor_tex = 'Assets/Level Assets/PNG/Tiles/tile_96.png'
ulcorner = 'Assets/Level Assets/PNG/Tiles/tile_280.png'
llcorner = 'Assets/Level Assets/PNG/Tiles/tile_307.png'
urcorner = 'Assets/Level Assets/PNG/Tiles/tile_281.png'
lrcorner = 'Assets/Level Assets/PNG/Tiles/tile_308.png'
capwall_l = 'Assets/Level Assets/PNG/Tiles/tile_313.png'
capwall_r = 'Assets/Level Assets/PNG/Tiles/tile_285.png'
capwall_u = 'Assets/Level Assets/PNG/Tiles/tile_312.png'
capwall_d = 'Assets/Level Assets/PNG/Tiles/tile_286.png'
floor = pygame.image.load(floor_tex)
wall_side = pygame.image.load(walls)
wall_up = pygame.image.load(wallu)
wall_uleft_corner = pygame.image.load(ulcorner)
wall_lleft_corner = pygame.image.load(llcorner)
wall_lright_corner = pygame.image.load(lrcorner)
wall_uright_corner = pygame.image.load(urcorner)
cwall_l = pygame.image.load(capwall_l)
cwall_r = pygame.image.load(capwall_r)
cwall_u = pygame.image.load(capwall_u)
cwall_d = pygame.image.load(capwall_d)
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
    global wall_rect
    pos_x = offset_x + x * tile_size
    pos_y = offset_y + y * tile_size

    if tile_type == 'wall_side':
        screen.blit(wall_side, (pos_x, pos_y))
        wall_rect = wall_side.get_rect()
    elif tile_type == 'wall_up':
        screen.blit(wall_up, (pos_x, pos_y))
    elif tile_type == 'uleft_corner':
        screen.blit(wall_uleft_corner, (pos_x, pos_y))
    elif tile_type == 'lleft_corner':
        screen.blit(wall_lleft_corner, (pos_x, pos_y))
    elif tile_type == 'lright_corner':
        screen.blit(wall_lright_corner, (pos_x, pos_y))
    elif tile_type == 'uright_corner':
        screen.blit(wall_uright_corner, (pos_x, pos_y))
    elif tile_type == 'floor':
        screen.blit(floor, (pos_x, pos_y))
    elif tile_type == 'cwall_d':
        screen.blit(cwall_d, (pos_x, pos_y))
    elif tile_type == 'cwall_u':
        screen.blit(cwall_u, (pos_x, pos_y))
    elif tile_type == 'cwall_l':
        screen.blit(cwall_l, (pos_x, pos_y))
    elif tile_type == 'cwall_r':
        screen.blit(cwall_r, (pos_x, pos_y))
    else:
        print(f"Unknown tile: {tile_type}")


