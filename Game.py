import pygame
from background import drawing
from Level_builder import build_level
from movement import move
from globals import P1, Level
###########################INITIALIZATION CONDITIONS#############################
pygame.init() # pygame setup
clock = pygame.time.Clock() #initializes the internal clock for frames and shtuff
running = True #flag for game to run
pygame.display.set_caption("Scrolling Background")
#################################################################################

build_level(Level)

while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
    drawing()#calls background.py to create the scrolling background
    build_level(Level)
    P1.draw()
    move()

    pygame.display.flip() # Update the full display Surface to the screen
    clock.tick(60) # Control frame rate

pygame.quit()