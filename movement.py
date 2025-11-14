import pygame
import math
from globals import P1, solid_tiles, debug_settings
from background import screen

pygame.init()


def move(dt, clock):
    
     #counts the amount of frames since last call of this function

    keys = pygame.key.get_pressed() #Returns state of all keys on the keyboard
    
    dx, dy = 0, 0 #Translation values

    w_bypass = False
    s_bypass = False
    a_bypass = False
    d_bypass = False
    if keys[pygame.K_w]:
        if not w_bypass:
            dy += 1
    if keys[pygame.K_s]:
        if not s_bypass:
            dy -= 1
    if keys[pygame.K_a]:
        if not a_bypass:
            dx += 1
    if keys[pygame.K_d]:
        if not d_bypass:
            dx -= 1

    #Normalize diagonal movement
    if dx != 0 or dy != 0: 
        length = math.sqrt(dx ** 2 + dy ** 2) 
        dx /= length
        dy /= length


    P1.x += dx * P1.speed * dt
    P1.y += dy * P1.speed * dt

##########################four thin squares placed at edges for collision########################

    if debug_settings:
        font = pygame.font.Font(None, 30)
        text_surface = font.render(f"Dx: {dx * P1.speed * dt} Dy: {dy * P1.speed * dt} Px: {P1.x} Py: {P1.y}", True, (255, 255, 255))
        text_rect = text_surface.get_rect(midleft=(10, 20))

        screen.blit(text_surface, text_rect)

        font = pygame.font.Font(None, 30)
        text_surface = font.render(f"Frames: {int(clock.get_fps())}", True, (255, 255, 255))
        text_rect = text_surface.get_rect(midleft=(800, 20))
        screen.blit(text_surface, text_rect)

