import pygame
from globals import enemy_group, enemy_bullet_group, bullet_group
from background import screen
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
            if len(enemy_group) < 10:
                if random.randint(0,100) >= 93:
                    self.enemy = Enemy(e_path, coords)
                    enemy_group.add(self.enemy)

    def draw(self):
        screen.blit(self.surface, self.rect)
        try:
            self.enemy.spawn()
        except:
            pass

    def update(self, xtrans, ytrans):
        self.coords[0] -= xtrans
        self.coords[1] -= ytrans
        self.rect = self.surface.get_rect(topleft = self.coords)
        for bullet in enemy_bullet_group:
            if bullet.rect.colliderect(self.rect) and self.name != "floor":
                bullet.kill()
        for bullet in bullet_group:
            if bullet.rect.colliderect(self.rect) and self.name != "floor":
                bullet.kill()
        try:   
            self.enemy.update(self.rect)
        except:
            pass
        