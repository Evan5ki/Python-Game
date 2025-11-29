from Enemy import Enemy
import random
from globals import enemy_list, built_tiles
enemy_count = 0


def generate_enemies():
    for tile in built_tiles:
        if tile.name == "floor":
            if random.randint(0,10) >= 9:
                enemy = Enemy("Assets/Level Assets/PNG/Soldier 1/soldier1_machine.png")
                enemy_list.append(enemy)

def rand_Spawn():
    for enemy in enemy_list:
        enemy.spawn()