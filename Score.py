import pygame
from background import screen, Width, Height
from globals import score

def update_score():
    font = pygame.font.Font(None, 30)
    scores = font.render(f"Score: {score}", True, (255, 255, 255))
    score_rect = scores.get_rect(midleft=(Width*0.01, Height* 0.02))
    screen.blit(scores, score_rect)

def score_update(points):
    global score
    score += points