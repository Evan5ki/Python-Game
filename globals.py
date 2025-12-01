import pygame
Level = [
    ['uleft_corner', 'wall_side', 'wall_side', 'wall_side', 'uright_corner', 'empty',     'empty',     'uleft_corner',  'wall_side', 'wall_side', 'uright_corner'],
    ['cwall_d',      'floor',     'floor',     'floor',     'lleft_corner',  'wall_side', 'wall_side', 'lright_corner', 'floor',     'floor',     'wall_up'],
    ['floor',        'floor',     'floor',     'floor',     'floor',         'floor',     'floor',     'floor',         'floor',     'floor',     'wall_up'],
    ['cwall_u',      'floor',     'floor',     'floor',     'uleft_corner',  'wall_side', 'wall_side', 'uright_corner', 'floor',     'floor',     'wall_up'],
    ['lleft_corner', 'wall_side', 'wall_side', 'wall_side', 'lright_corner', 'empty',     'empty',     'lleft_corner',  'wall_side', 'wall_side', 'lright_corner']
]
Loaded_Level = [

]
Level_1 = [
    ['uleft_corner', 'wall_side', 'uright_corner'],
    ['wall_up', 'floor', 'wall_up'],
    ['lleft_corner', 'wall_side', 'lright_corner']
]

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

Assets = {

}

built_tiles = [
    
]
enemy_list = [

]


Active_level = Level

bullet_group = pygame.sprite.Group()
enemy_bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
score = 0
tile_size = 100
scale = tile_size/64
initial = True
running = True

xtrans = 0
ytrans = 0

debug_settings = False