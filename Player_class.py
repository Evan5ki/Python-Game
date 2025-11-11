import pygame
import math
from background import screen, Width, Height

class Player:
    def __init__(self, speed, health, path, x, y):
        self.speed = speed
        self.health = health
        self.x = x
        self.y = y
        self.image = pygame.image.load(path).convert_alpha()

        # Fixed collision rect (does not rotate)
        self.rect = self.image.get_rect(center=(Width // 2, Height // 2))
        self.angle = 0
        self.render = self.image  # start with unrotated sprite

    def update_render(self):
        """Rotate the player's image visually, but keep rect fixed."""
        self.angle = self.get_angle()

        # Rotate sprite only for drawing
        rotated_image = pygame.transform.rotate(self.image, self.angle)

        # Get a rect for drawing the rotated image, centered on the fixed rect
        self.render = rotated_image
        self.render_rect = rotated_image.get_rect(center=self.rect.center)

    def draw(self):
        """Draw the player."""
        self.update_render()

        screen.blit(self.render, self.render_rect)


    def get_angle(self):
        """Calculate the rotation angle between player center and mouse position."""
        mx, my = pygame.mouse.get_pos()
        dx = mx - self.rect.centerx
        dy = my - self.rect.centery
        return -math.degrees(math.atan2(dy, dx))
