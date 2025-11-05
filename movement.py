import pygame
import math
import globals



pygame.init()

clock = pygame.time.Clock()
clock = clock.tick(60)

def move():
    dt = clock / 1000 #counts the amount of frames since last call of this function

    keys = pygame.key.get_pressed() #Returns state of all keys on the keyboard
    
    dx, dy = 0, 0 #Translation values
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
    globals.P1.x += dx * globals.P1.speed * dt
    globals.P1.y += dy * globals.P1.speed * dt
    
