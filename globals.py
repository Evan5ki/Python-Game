from Player_class import Player

collision = False

P1 = Player(3, 100, 'Assets/Level Assets/PNG/Hitman 1/hitman1_stand.png', 0, 0)

tile_size = 100
scale = tile_size/64

Level = [
    ['uleft_corner', 'wall_side', 'wall_side', 'wall_side', 'uright_corner', 'empty',     'empty',     'uleft_corner',  'wall_side', 'wall_side', 'uright_corner'],
    ['cwall_d',      'floor',     'floor',     'floor',     'lleft_corner',  'wall_side', 'wall_side', 'lright_corner', 'floor',     'floor',     'wall_up'],
    ['floor',        'floor',     'floor',     'floor',     'floor',         'floor',     'floor',     'floor',         'floor',     'floor',     'wall_up'],
    ['cwall_u',      'floor',     'floor',     'floor',     'uleft_corner',  'wall_side', 'wall_side', 'uright_corner', 'floor',     'floor',     'wall_up'],
    ['lleft_corner', 'wall_side', 'wall_side', 'wall_side', 'lright_corner', 'empty',     'empty',     'lleft_corner',  'wall_side', 'wall_side', 'lright_corner']
]
Level_1 = [
    ['uleft_corner', 'wall_side', 'uright_corner'],
    ['empty', 'empty', 'empty'],
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

solid_tiles = [

]


