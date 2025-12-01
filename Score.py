import pygame
from background import screen, Width, Height
from globals import score, debug_settings

def update_score(P1):
    if not debug_settings:
        font = pygame.font.Font(None, 30)
        scores = font.render(f"Score: {score}", True, (255, 255, 255))
        score_rect = scores.get_rect(midleft=(Width*0.01, Height* 0.02))
        screen.blit(scores, score_rect)
        Health = font.render(f"Health: {P1.health}", True, (255, 255, 255))
        health_rect = Health.get_rect(topleft = score_rect.bottomleft)
        screen.blit(Health, health_rect)
        rounds = font.render(f"Bullets: {P1.bullets}", True, (255, 255, 255))
        rounds_rect = rounds.get_rect(topleft = health_rect.bottomleft)
        screen.blit(rounds, rounds_rect)

def score_update(points):
    if not debug_settings:
        global score
        score += points