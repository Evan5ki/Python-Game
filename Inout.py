import pygame
from background import screen, Width, Height
from Button import Button
import globals
def title_screen():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        font = pygame.font.Font(None, 200)
        surface = font.render(f"HITMAN", True, (255, 255, 255))
        rect = surface.get_rect(center=(Width//2, Height//2-50))
        screen.blit(surface, rect)
        begin = Button(Width//2, Height//2 + 100, "PLAY")
        begin.update()
        if begin.event_handler():
            break
        pygame.display.flip()
    


def end(P1):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        font = pygame.font.Font(None, 175)
        surface = font.render(f"YOU DIED", True, (255, 0, 0))
        rect = surface.get_rect(center=(Width//2, Height//2))
        screen.blit(surface, rect)
        restart = Button(Width//2, Height//2 + 150, "PLAY AGAIN")
        restart.update()
        if restart.event_handler():
            screen.fill((0, 0, 0))
            clean_house(P1)
            break
        pygame.display.flip()

def clean_house(P1):
    P1.x = Width // 2
    P1.y = Height // 2
    P1.health = 100
    globals.enemy_group.empty()
    globals.bullet_group.empty()
    globals.initial = True
    globals.running = True
    globals.Loaded_Level.clear()