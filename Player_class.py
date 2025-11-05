import pygame
from background import screen, Width, Height
import math

Mx, My = 0, 0

class Player:
    def __init__(self, speed, health, path, x, y):
        self.speed = speed
        self.health = health
        self.path = path
        self.x = x
        self.y = y
        rend, rect = self.load()
        self.render = rend
        self.rect = rect
        

    def draw(self):
        rend, rect = self.load()
        screen.blit(rend, rect)
    
    def load(self):
        loaded = pygame.image.load(self.path).convert_alpha()
        render = pygame.transform.rotate(loaded, self.get_angle())#transforms the image 
        P1_Center = (Width/2 + 8, Height/2)
        P1_Rect = render.get_rect(center = P1_Center)
        self.rect = P1_Rect
        return render, P1_Rect
    
    def get_angle(self): #calculates the angle at which to rotate the character
        Mx, My = pygame.mouse.get_pos() #Loads mouse coords to respective coordinates
        Mx -= Width/2 #Centers 0,0 to the center of the screen and not top left
        My -= Height/2
        
        if Mx == 0:
            if My < 0: #handles divide by zero
                return 90
            else:
                return -90
        else:
            return math.degrees(-math.atan2(My, Mx)) #Calculates angle between the origin and the mouse

