import pygame


#################################################################################
###########################INITIALIZATION CONDITIONS#############################
pygame.init() # pygame setup
Width = 1080 #graphics
Height = 700
screen = pygame.display.set_mode((Width, Height))
clock = pygame.time.Clock() #initializes the internal clock for frames and shtuff
running = True #flag for game to run
pygame.display.set_caption("Scrolling Background")
#################################################################################
##########################BACKGROUND INITIALIZATION##############################
background_image = pygame.image.load("Assets/stars.jpg").convert()
background_image = pygame.transform.scale(background_image, (Width, Height))
back_y = 0
back_y1 = -background_image.get_height() 
back_x = 0
back_x1 = -background_image.get_width()
scroll_speed = 0.75
#################################################################################
#################################################################################

def draw():
    global back_x, back_x1, back_y, back_y1

    back_y += scroll_speed
    back_y1 += scroll_speed
    back_x += scroll_speed
    back_x1 += scroll_speed

    # Reset positions when they go off-screen to create a loop
    if back_y >= Height:
        back_y = -background_image.get_height()
    if back_y1 >= Height:
        back_y1 = -background_image.get_height()
    if back_x >= Width:
        back_x = -background_image.get_width()
    if back_x1 >= Width:
        back_x1 = -background_image.get_width()

    # Draw the backgrounds
    screen.blit(background_image, (back_x, back_y))
    screen.blit(background_image,(back_x1, back_y))
    screen.blit(background_image,(back_x, back_y1))
    screen.blit(background_image, (back_x1, back_y1))


while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    draw()

    pygame.display.flip() # Update the full display Surface to the screen
    clock.tick(60) # Control frame rate

pygame.quit()