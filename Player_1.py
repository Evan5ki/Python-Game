import pygame
from background import screen, Width, Height
import math
pygame.init()

P1 = 'Assets/Level Assets/PNG/Hitman 1/hitman1_gun.png'


P1_Image = pygame.image.load(P1).convert_alpha()
P1_Width, P1_Height = P1_Image.get_size()
P1_Rect = P1_Image.get_rect()
P1_Center = (Width/2 + 8, Height/2)
last_theta = 0
Mx, My = 0, 0

def load_P1():
    pygame.draw.circle(screen, (255, 0, 0), (1080/2, 700/2), 1)
    

    P1_Final = pygame.transform.rotate(P1_Image, get_angle())

    P1_Rect = P1_Final.get_rect(center=P1_Center)
    print(get_angle())
    screen.blit(P1_Final, P1_Rect)


def get_angle():
    Mx, My = pygame.mouse.get_pos()
    Mx -= Width/2
    My -= Height/2
    
    if Mx == 0:
        if My < 0:
            return 90
        else:
            return -90
    else:
        return math.degrees(-math.atan2(My, Mx))
    