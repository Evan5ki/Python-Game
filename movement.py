import pygame
import math
pygame.init()
from Player_1 import player



def move(clock):

    dt = clock / 1000

    keys = pygame.key.get_pressed()

    dx, dy = 0, 0
    if keys[pygame.K_w]:
        dy += 1
    if keys[pygame.K_s]:
        dy -= 1
    if keys[pygame.K_a]:
        dx += 1
    if keys[pygame.K_d]:
        dx -= 1

    # --- Normalize diagonal movement ---
    if dx != 0 or dy != 0:
        length = math.sqrt(dx ** 2 + dy ** 2)
        dx /= length
        dy /= length

    player["x"] += dx * player["speed"] * dt
    player["y"] += dy * player["speed"] * dt

    


