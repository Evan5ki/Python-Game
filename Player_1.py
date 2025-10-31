import pygame
from background import screen, Width, Height
import math
pygame.init()

P1 = 'Assets/Level Assets/PNG/Hitman 1/hitman1_gun.png'


P1_Image = pygame.image.load(P1).convert_alpha()#loads image without background
P1_Width, P1_Height = P1_Image.get_size() #loads the values of the image width and height
P1_Rect = P1_Image.get_rect() #creates a rectangle to go under it
P1_Center = (Width/2 + 8, Height/2) #point about which to rotate
last_theta = 0
Mx, My = 0, 0

def load_P1():
    P1_Final = pygame.transform.rotate(P1_Image, get_angle())#transforms the image 
    P1_Rect = P1_Final.get_rect(center = P1_Center) #transforms the rectangle position

    screen.blit(P1_Final, P1_Rect)#draws P1


def get_angle(): #calculates the angle at which to rotate the character
    Mx, My = pygame.mouse.get_pos()
    Mx -= Width/2
    My -= Height/2
    
    if Mx == 0:
        if My < 0: #handles divide by zero
            return 90
        else:
            return -90
    else:
        return math.degrees(-math.atan2(My, Mx))
    