import pygame
from globals import tile_size, scale, Asset_names
from background import Width, Height, screen

class Tile:
    def __init__(self, x, y, rectangle):
        self.x = x
        self.y = y
        self.rect = rectangle

    def draw(self):
        pygame.draw.rect(screen, (255,0,0), self.rect)