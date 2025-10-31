import pygame
from background import Width, Height, screen
pygame.init()


tile_size = 64

walls = 'Assets/Level Assets/PNG/Tiles/tile_282.png'
wallu = 'Assets/Level Assets/PNG/Tiles/tile_309.png'
floor_tex = 'Assets/Level Assets/PNG/Tiles/tile_96.png'
ulcorner = 'Assets/Level Assets/PNG/Tiles/tile_280.png'
llcorner = 'Assets/Level Assets/PNG/Tiles/tile_307.png'
urcorner = 'Assets/Level Assets/PNG/Tiles/tile_281.png'
lrcorner = 'Assets/Level Assets/PNG/Tiles/tile_308.png'


floor = pygame.image.load(floor_tex)
wall_side = pygame.image.load(walls)
wall_up = pygame.image.load(wallu)
wall_uleft_corner = pygame.image.load(ulcorner)
wall_lleft_corner = pygame.image.load(llcorner)
wall_lright_corner = pygame.image.load(lrcorner)
wall_uright_corner = pygame.image.load(urcorner)


Level = [
    ['uleft_corner', 'wall_side', 'wall_side', 'wall_side', 'uright_corner'],
    ['wall_up', 'floor', 'floor', 'floor', 'wall_up'],
    ['wall_up', 'floor', 'floor', 'floor', 'wall_up'],
    ['wall_up', 'floor', 'floor', 'floor', 'wall_up'],
    ['lleft_corner', 'wall_side', 'wall_side', 'wall_side', 'lright_corner']
]



def build_level(level):
    for y, value in enumerate(level):
        for x, cell in enumerate(value):
            build_wall(x, y, cell)


def build_wall(x, y, type):
    l_width, l_height = total_width()

    if type == 'wall_side':
        screen.blit(wall_side, (Width - ###########SOLVE THE POSITIONING ISSUE#######################WORKING HERE#####################tile_size*x, tile_size*y))
    elif type == 'wall_up':
        screen.blit(wall_up, (tile_size*x, tile_size*y))
    elif type == 'uleft_corner':
        screen.blit(wall_uleft_corner, (tile_size*x, tile_size*y))
    elif type == 'lleft_corner':
        screen.blit(wall_lleft_corner, (tile_size*x, tile_size*y))
    elif type == 'lright_corner':
        screen.blit(wall_lright_corner, (tile_size*x, tile_size*y))
    elif type == 'uright_corner':
        screen.blit(wall_uright_corner, (tile_size*x, tile_size*y))
    elif type == 'floor':
        screen.blit(floor, (tile_size*x, tile_size*y))
    else:
        print("uh oh")

def total_width():
    level_height = len(Level)
    level_width = len(Level[0])
    return level_width, level_height