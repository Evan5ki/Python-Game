import pygame
import math
from background import screen, Width, Height

class Player:
    def __init__(self, speed, health, path, x, y):
        self.speed = speed
        self.health = health
        self.path = path
        self.x = x
        self.y = y

        self.image = pygame.image.load(self.path).convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.angle = 0
        self.update_render()

    def update_render(self):
        """Update the player's rotated image and rect based on mouse angle."""
        self.angle = self.get_angle()
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        center = (Width / 2, Height / 2)
        self.rect = rotated_image.get_rect(center=center)
        self.render = rotated_image

    def draw(self):
        """Draw the player"""
        self.update_render()
        screen.blit(self.render, self.rect)

        mask_surface = self.mask.to_surface(setcolor=(255, 255, 255),
                                            unsetcolor=(0, 0, 0, 0))
        mask_surface.set_alpha(100)
        mask_surface = pygame.transform.rotate(mask_surface, self.angle)
        screen.blit(mask_surface, self.rect)



















    def get_angle(self):
        """Calculate the rotation angle between player center and mouse position."""
        mx, my = pygame.mouse.get_pos()
        dx = mx - Width / 2
        dy = my - Height / 2
        return -math.degrees(math.atan2(dy, dx))
