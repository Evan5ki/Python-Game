import pygame
from background import screen, Width, Height
from globals import Loaded_Level, enemy_group
from Score import score_update

import math
image = 'Assets/Player Assets/bullet.png'
class Bullet(pygame.sprite.Sprite):
    def __init__(self, angle, super_rect, friend):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect()
        self.rect = self.rect.inflate(-10,-10)
        self.angle = math.radians(angle)
        self.speed = 10
        self.friendly = friend
        self.x = super_rect.x
        self.y = super_rect.y
        self.rect.center = (self.x, self.y)

    def update(self, xtrans, ytrans, P1):
        self.rect.x -= self.speed * math.cos(self.angle) * -1 + xtrans
        self.rect.y += self.speed * math.sin(self.angle) * -1 - ytrans
        self.draw()

    
    def draw(self):
        screen.blit(self.image, self.rect)