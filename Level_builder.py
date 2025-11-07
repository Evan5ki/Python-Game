import pygame
from background import Width, Height, screen
from globals import P1


pygame.init()

tile_size = 100
scale = tile_size/64

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

for i, value in enumerate(Asset_paths):
    name = Asset_names[i]
    image = pygame.image.load(value)
    image = pygame.transform.rotozoom(image,0,scale)
    rect = image.get_rect(center = (tile_size//2,tile_size//2))

    Assets[name] = {
        "image": image,
        "rect" : rect
    }
###############################################ASSET INITIALIZATION####################################

lists = []
def build_level(level): #builds the level by calling build tile for each element in the level list
    lists.clear()
    level_width = len(level[0]) * tile_size #sets width of the level
    level_height = len(level) * tile_size #sets height of the level
    offset_x = (Width - level_width) // 2 
    offset_y = (Height - level_height) // 2
    for y, row in enumerate(level):
        for x, cell in enumerate(row):
            a = build_tile(x + P1.x, y + P1.y, cell, offset_x, offset_y)
            if cell != 'floor' and cell != 'empty':
                lists.append(a)
            
            

    



def build_tile(x, y, tile_type, offset_x, offset_y): #Builds each tile in the correct location
    pos_x = offset_x + x * tile_size
    pos_y = offset_y + y * tile_size
    if tile_type not in Assets:
        pass
    else:
        image = Assets[tile_type]["image"]
        tile_rect = image.get_rect(topleft=(pos_x, pos_y))
        screen.blit(image, (pos_x, pos_y))
        return tile_rect 
        """
        if tile_type != 'floor':
            pygame.draw.rect(screen, (255, 0, 0), tile_rect)
        """
    










""" collision stuff to come back to
if tile_type in Assets:
        
        if hasattr(P1, "rect") and P1.rect.colliderect(tile_rect) and tile_type != "floor": #Checks how a tile is overlapped with the player
            if P1.rect.bottom > tile_rect.top and P1.rect.top < tile_rect.top:
                print("Player hit tile from top")
                globals.collision = True
            elif P1.rect.top < tile_rect.bottom and P1.rect.bottom > tile_rect.bottom:
                print("Player hit tile from bottom")
                globals.collision = True
            elif P1.rect.right > tile_rect.left and P1.rect.left < tile_rect.left:
                print("Player hit tile from left")
            elif P1.rect.left < tile_rect.right and P1.rect.right > tile_rect.right:
                print("Player hit tile from right")
"""