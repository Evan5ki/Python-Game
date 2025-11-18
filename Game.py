import pygame
from background import draw_background
from Level_builder import build_level, let_there_be_level
from globals import P1, Level, Level_1
from debugger import debug
from Inout import title, end
###########################INITIALIZATION CONDITIONS#############################
pygame.init() # pygame setup
running = True #flag for game to run
pygame.display.set_caption("PYGAME!")
clock = pygame.time.Clock()
#################################################################################
Playerx = 0
Playery = 0
while running:
    ####Allows to quit the game###########
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    ######################################
    
    #Sets the target framerate and global clock#
    dt = clock.tick(60)
    ############################################
    
    ##Starts the background sequence ## background.py ##
    draw_background() ##Checked and finished
    ####################################################
    temp_player_tuple = P1.move(dt)
    Playerx -= temp_player_tuple[0]
    Playery -= temp_player_tuple[1] 
    ##Takes in the Level array and builds it ## Level_builder.py ##
    TILES = build_level(Level, Playerx, Playery)
    ###############################################################
    P1.check_collision(TILES)
    
    let_there_be_level()
    P1.draw()

    #turns on debug settings if True in globals ## debugger.py ##
    debug(clock)
    #############################################################
     
    #end()



    pygame.display.flip() # Update the full display Surface to the screen
pygame.quit()