import pygame

#################################################################################
###########################INITIALIZATION CONDITIONS#############################
pygame.init() # pygame setup
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock() #initializes the internal clock for frames and shtuff
running = True #flag for game to run
#################################################################################

fullscreen = False

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_RETURN and pygame.key.get_mods() & event.type == pygame.KMOD_LALT:
                fullscreen = not fullscreen
                if fullscreen == False:
                    pygame.display.set_mode(500,500)
                elif fullscreen == True:
                    pygame.display.set_mode((0,0), pygame.FULLSCREEN)
            
    screen.fill((30, 30, 30))
    pygame.display.flip()
    clock.tick(144)  # limits FPS to 60

pygame.quit()