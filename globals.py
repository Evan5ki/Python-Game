from Player_class import Player

wall_collision = False

P1 = Player(4, 100, 'Assets/Level Assets/PNG/Hitman 1/hitman1_stand.png', 0, 0)

Level = [
    ['uleft_corner', 'wall_side', 'wall_side', 'wall_side', 'uright_corner', 'empty',     'empty',     'uleft_corner',  'wall_side', 'wall_side', 'uright_corner'],
    ['cwall_d',      'floor',     'floor',     'floor',     'lleft_corner',  'wall_side', 'wall_side', 'lright_corner', 'floor',     'floor',     'wall_up'],
    ['floor',        'floor',     'floor',     'floor',     'floor',         'floor',     'floor',     'floor',         'floor',     'floor',     'wall_up'],
    ['cwall_u',      'floor',     'floor',     'floor',     'uleft_corner',  'wall_side', 'wall_side', 'uright_corner', 'floor',     'floor',     'wall_up'],
    ['lleft_corner', 'wall_side', 'wall_side', 'wall_side', 'lright_corner', 'empty',     'empty',     'lleft_corner',  'wall_side', 'wall_side', 'lright_corner']
]