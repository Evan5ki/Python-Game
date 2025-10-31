import pygame
from background import drawing
from Player_1 import load_P1
from Level_1 import build_level, Level
###########################INITIALIZATION CONDITIONS#############################
pygame.init() # pygame setup
clock = pygame.time.Clock() #initializes the internal clock for frames and shtuff
running = True #flag for game to run
pygame.display.set_caption("Scrolling Background")
#################################################################################





while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    drawing()#calls background.py to create the scrolling background
    build_level(Level)
    load_P1()

    pygame.display.flip() # Update the full display Surface to the screen
    clock.tick(100) # Control frame rate

pygame.quit()