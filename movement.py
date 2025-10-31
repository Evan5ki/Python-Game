import pygame
from Level_builder import wall_rect
from Player_1 import P1_Rect
pygame.init()



player = {"x": 0, "y": 0, "speed": 0.05}

def move():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if(P1_Rect.colliderect(wall_rect)):
            player["y"] -= player["speed"]
        else:
            player["y"] += player["speed"]
    elif keys[pygame.K_a]:
        player["x"] += player["speed"]
    elif keys[pygame.K_s]:
        player["y"] -= player["speed"]
    elif keys[pygame.K_d]:
        player["x"] -= player["speed"]


