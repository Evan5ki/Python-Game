import pygame
from background import draw_background, Width, Height, screen
from Level_builder import load_level, update_tiles, draw_tiles
from debugger import debug
from Player_class import Player
from Inout import title_screen, end
from enemy_builder import rand_Spawn, generate_enemies
from Score import update_score
import globals
###########################INITIALIZATION CONDITIONS#############################
pygame.init() # pygame setup
 #flag for game to run
pygame.display.set_caption("PYGAME!")
clock = pygame.time.Clock()
#################################################################################

P1 = Player(0.3, 100, 'Assets/Level Assets/PNG/Hitman 1/hitman1_stand.png')
while globals.running:
    ####Allows to quit the game###########
    ######################################
    if globals.initial:
        title_screen()
        load_level()
        globals.initial = False
        #generate_enemies()
    #Sets the target framerate and global clock#
    dt = clock.tick(60)
    ############################################
    
    ##Starts the background sequence ## background.py ##
    draw_background() ##Checked and finished
    ####################################################
    player_vectors = P1.move(dt)
    ##Takes in the Level array and builds it ## Level_builder.py ##
    ###############################################################
    #P1.check_collision(TILES)
    update_tiles(player_vectors[0], player_vectors[1])
    P1.check_collision(player_vectors)
    if P1.check_collision(player_vectors):
        update_tiles(-player_vectors[0]*0, -player_vectors[1]*1)
    #rand_Spawn()
    draw_tiles()
    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    P1.shoot()
    globals.bullet_group.update()
    P1.draw()
    update_score()
    #turns on debug settings if True in globals ## debugger.py ##
    debug(clock, P1)
    #############################################################
    if P1.health <= 0:
        end(P1)
        print(globals.initial)
    pygame.display.flip() # Update the full display Surface to the screen



