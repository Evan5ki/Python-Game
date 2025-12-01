import pygame
import random
import math

from globals import enemy_bullet_group, bullet_group
from Score import score_update
from bullet import Bullet
from background import screen, Width, Height
class Enemy(pygame.sprite.Sprite):
    def __init__(self, path, coords):
        super().__init__()
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect(topleft = coords)
        self.path = path
        self.rotate_image = 0
        self.rotate_rect = 0
        self.time = pygame.time.get_ticks()
      
    def get_p_angle(self):
        dx = Width//2 - self.rect.centerx
        dy = Height//2 - self.rect.centery
        return -math.degrees(math.atan2(dy, dx))
    
    def shoot(self):
        if self.alive():
            if (pygame.time.get_ticks() - self.time) > 2000:
                bullet = Bullet(self.get_p_angle(), self.rect, False)
                enemy_bullet_group.add(bullet)
    
    def update(self, tile):
        self.rect.center = tile.center
        self.rotate_image = pygame.transform.rotate(self.image, self.get_p_angle())
        self.rotate_rect = self.rotate_image.get_rect(center = self.rect.center)
        if random.randint(0,1000) > 985:
            self.shoot()
        for bullet in bullet_group:
            if bullet.rect.colliderect(self.rect):
                self.kill()
                bullet.kill()
                hit_sound = pygame.mixer.Sound('Assets/cod-hitmarker-made-with-Voicemod.wav')
                hit_sound.play()
                score_update(100)
                self.rect = 0

    def spawn(self):
        if self.alive():
            screen.blit(self.rotate_image, self.rotate_rect)

        