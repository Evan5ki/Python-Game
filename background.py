import pygame


pygame.init()

background = 'Assets/stars.jpg' # change for a new background
Width = 500 #graphics
Height = 500


screen = pygame.display.set_mode((Width, Height))

background_image = pygame.image.load(background).convert()
background_image = pygame.transform.scale(background_image, (Width, Height))


back_y = 0
back_y1 = -background_image.get_height() 
back_x = 0
back_x1 = -background_image.get_width()
scroll_speed = 0.25



def drawing():
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