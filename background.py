import pygame
from Game import Width, Height, screen
background_image = pygame.image.load("Assets/stars.jpg").convert()
background_image = pygame.transform.scale(background_image, (Width, Height))
backy = 0
backy1 = -background_image.get_height() 
backx = 0
backx1 = -background_image.get_width()

# Position the second image above the first
scroll_speed = 0.75 # Adjust as needed


while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update background positions
    backy += scroll_speed
    backy1 += scroll_speed
    backx += scroll_speed
    backx1 += scroll_speed
    # Reset positions when they go off-screen to create a loop

    if backy >= Height:
        backy = -background_image.get_height()
    if backy1 >= Height:
        backy1 = -background_image.get_height()
    if backx >= Width:
        backx = -background_image.get_width()
    if backx1 >= Width:
        backx1 = -background_image.get_width()
    # Draw the backgrounds
    screen.blit(background_image, (backx, backy))
    screen.blit(background_image,(backx1, backy))
    screen.blit(background_image,(backx, backy1))
    screen.blit(background_image, (backx1, backy1))

    pygame.display.flip() # Update the full display Surface to the screen
    clock.tick(60) # Control frame rate

pygame.quit()
