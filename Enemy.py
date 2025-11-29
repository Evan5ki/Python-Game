import pygame
import random
import math

from globals import Active_level
from background import screen, Width, Height
class Enemy(pygame.sprite.Sprite):
    def __init__(self, path, coords):
        super().__init__()
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect(topleft = coords)
        self.path = path
        self.rotate_image = 0
        self.rotate_rect = 0
      
    def get_p_angle(self):
        dx = Width//2 - self.rect.centerx
        dy = Height//2 - self.rect.centery
        return -math.degrees(math.atan2(dy, dx))
    
    def update(self, tile):
        self.rect.center = tile.center
        self.rotate_image = pygame.transform.rotate(self.image, self.get_p_angle())
        self.rotate_rect = self.rotate_image.get_rect(center = self.rect.center)

    def spawn(self):
        if self.alive():
            screen.blit(self.rotate_image, self.rotate_rect)
            pygame.draw.rect(screen, (0,255,0), self.rect, 2)