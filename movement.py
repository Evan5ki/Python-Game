import pygame
import math
from globals import P1, solid_tiles, Assets
from background import screen




pygame.init()

clock = pygame.time.Clock()

debug_settings = True

def move():

    dt = clock.tick(60) / 1000 #counts the amount of frames since last call of this function

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


    copy_rect = P1.rect.copy()

    copy_rect.x += -4 * dx
    copy_rect.y += -4 * dy
    x_hit = False
    y_hit = False
    i = 0
    for tile in solid_tiles:
        if copy_rect.colliderect(tile):
            if copy_rect.top <= tile.rect.bottom and P1.rect.top > tile.rect.bottom:
                i+=1
                print(i)
            x_hit = True
            y_hit = True
            
    if not x_hit and not y_hit:
        P1.x += dx * P1.speed * dt
        P1.y += dy * P1.speed * dt



    if debug_settings:
        font = pygame.font.Font(None, 30)
        text_surface = font.render(f"Dx: {int(P1.x)}", True, (255, 255, 255))
        text_rect = text_surface.get_rect(midleft=(10, 20))

        screen.blit(text_surface, text_rect)
        font = pygame.font.Font(None, 30)
        text_surface = font.render(f"Dy: {int(P1.y)}", True, (255, 255, 255))
        text_rect = text_surface.get_rect(midleft=(10, 40))

        screen.blit(text_surface, text_rect)

