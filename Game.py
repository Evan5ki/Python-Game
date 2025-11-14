import pygame
from background import drawing
from Level_builder import build_level
from movement import move
from globals import P1, Level
###########################INITIALIZATION CONDITIONS#############################
pygame.init() # pygame setup
running = True #flag for game to run
pygame.display.set_caption("PYGAME!")
clock = pygame.time.Clock()
#################################################################################

while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
    dt = clock.tick(60)

    drawing()#calls background.py to create the scrolling background
    build_level(Level)
    move(dt, clock)
    P1.draw()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        P1.attack()
    P1.update(dt)       

    pygame.display.flip() # Update the full display Surface to the screen
    # Control frame rate
pygame.quit()