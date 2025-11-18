import pygame
from background import screen, Width, Height
from globals import i
def title():
    global i
    font = pygame.font.Font(None, 200)
    surface = font.render(f"HITMAN", True, (255, 255, 255))
    surface.set_alpha(i)
    rect = surface.get_rect(center=(Width//2, Height//2))
    screen.blit(surface, rect)
    if i > 0:
        i -= 1


def end():
    global i

    font = pygame.font.Font(None, 175)
    surface = font.render(f"YOU DIED", True, (255, 255, 255))
    rect = surface.get_rect(center=(Width//2, Height//2))
    screen.blit(surface, rect)