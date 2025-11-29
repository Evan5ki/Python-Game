import pygame
from background import screen, Width, Height
from globals import Loaded_Level, enemy_group
from Score import score_update

import math
image = 'Assets/Level Assets/PNG/Tiles/tile_241.png'
class Bullet(pygame.sprite.Sprite):
    def __init__(self, angle):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect = self.rect.inflate(-30, -30)
        self.angle = math.radians(angle)
        self.speed = 10
        self.x = Width//2
        self.y = Height//2
        self.rect.center = (self.x, self.y)

    def update(self):
        for tile in Loaded_Level:
            if tile.name != 'floor':
                if self.rect.colliderect(tile.rect):
                    self.kill()
        if self.rect.x < 0 or self.rect.x > Width:
            self.kill
        if self.rect.y < 0 or self.rect.y > Height:
            self.kill
        for enemy in enemy_group:
            if self.rect.colliderect(enemy.rect):
                self.kill()
                enemy.kill()
                score_update(100)
        self.rect.x -= self.speed * math.cos(self.angle) * -1
        self.rect.y += self.speed * math.sin(self.angle) * -1
        self.draw()
        
        #pass
    
    def draw(self):
        screen.blit(self.image, self.rect)