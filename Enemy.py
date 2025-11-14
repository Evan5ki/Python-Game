import pygame
from background import screen
import random
from globals import P1

enemy_sprite = 'Assets/Level Assets/PNG/Man Blue/manBlue_stand.png'


class Enemy:
    def __init__(self, x, y):
        self.image = pygame.transform.rotate(pygame.image.load(enemy_sprite).convert_alpha(), random.randint(0,360))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        


