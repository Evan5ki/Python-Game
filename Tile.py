import pygame
from globals import tile_size, scale, Asset_names
from background import Width, Height, screen

class Tile:
    def __init__(self, surface, coords, tile_name):
        self.surface = surface
        self.coords = coords
        self.rect = surface.get_rect(topleft = self.coords)
        self.name = tile_name

    def draw(self):
        pygame.draw.rect(screen, (255,0,0), self.rect)