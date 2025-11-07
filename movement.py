import pygame
import math
from globals import P1
from Level_builder import lists


pygame.init()

clock = pygame.time.Clock()

def move():
    dt = clock.tick(60) / 1000 #counts the amount of frames since last call of this function

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

    #Normalize diagonal movement
    if dx != 0 or dy != 0: 
        length = math.sqrt(dx ** 2 + dy ** 2) 
        dx /= length
        dy /= length

    #check each axis individually

    #reset position
    copy = P1.rect.copy()
    copy.x += dx * P1.speed * dt
    copy.y += dy * P1.speed * dt
    #if copy.collidelist(lists) != -1:
        #pass
    #else:
    P1.x += dx * P1.speed * dt
    P1.y += dy * P1.speed * dt



