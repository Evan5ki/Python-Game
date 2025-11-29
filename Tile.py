import pygame
from globals import tile_size, scale, Asset_names, enemy_group
from background import Width, Height, screen
from Enemy import Enemy
import random


e_path = "Assets/Level Assets/PNG/Soldier 1/soldier1_machine.png"
class Tile:
    def __init__(self, surface, coords, tile_name):
        self.surface = surface
        self.coords = coords
        self.rect = surface.get_rect(topleft = self.coords)
        self.name = tile_name
        if self.name == "floor":
            if random.randint(0,10) >= 9:
                self.enemy = Enemy(e_path, coords)
                enemy_group.add(self.enemy)

    def draw(self):
        screen.blit(self.surface, self.rect)
        pygame.draw.rect(screen, (255,0,0), self.rect, 2)
        try:
            self.enemy.spawn()
        except:
            pass

    def update(self, xtrans, ytrans):
        self.coords[0] -= xtrans
        self.coords[1] -= ytrans
        self.rect = self.surface.get_rect(topleft = self.coords)
        try:
            self.enemy.update(self.rect)
        except:
            pass
        