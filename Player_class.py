import pygame
import math
from background import screen, Width, Height


top = False
bottom = False
class Player:
    def __init__(self, speed, health, path):
        self.speed = speed
        self.health = health
        self.dx = 0
        self.dy = 0
        self.x = Width // 2
        self.y = Height // 2
        self.timer = 0
        self.angle = 0
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect(center=(Width // 2, Height // 2))
        self.render = self.image

    def move(self, dt):
        """Does the calculation for player displacement and passes it out to levelbuilder via main"""
        keys = pygame.key.get_pressed()
        self.dy = 0
        self.dx = 0
        if keys[pygame.K_w]:
                self.dy -= 1
        if keys[pygame.K_s]:
                self.dy += 1
        if keys[pygame.K_a]:
                self.dx -= 1
        if keys[pygame.K_d]:
                self.dx += 1
        if self.dx != 0 or self.dy != 0: 
            length = math.sqrt(self.dx ** 2 + self.dy ** 2) 
            self.dx /= length
            self.dy /= length
        xaxis = self.dx * self.speed * dt
        
        yaxis = self.dy * self.speed * dt
        if top == True and yaxis < 0:
             yaxis = 0
        if bottom == True and yaxis > 0:
             yaxis = 0####################################WOULD BE TRUE JUST CALLED BEFORE LOGIC HAPPENS FIX TMRW
        self.x += xaxis
        self.y += yaxis
        return xaxis, yaxis

    def draw(self):
        """Draws the player after calling the update function"""
        self.update_render()
        screen.blit(self.render, self.render_rect)
    
    def update_render(self):
        """Calls get angle for rotation value then calculates the new rectangles"""
        self.angle = self.get_angle()

        rotated_image = pygame.transform.rotate(self.image, self.angle)

        self.rect.center = (Width // 2, Height // 2)
        self.render = rotated_image
        self.render_rect = rotated_image.get_rect(center = self.rect.center)

    def get_angle(self):
        """Calculate the rotation angle between player center and mouse position."""
        mx, my = pygame.mouse.get_pos()
        dx = mx - self.rect.centerx
        dy = my - self.rect.centery
        return -math.degrees(math.atan2(dy, dx))
    
    def check_collision(self, tile_list):
        for tile in tile_list:
            if self.rect.colliderect(tile.rect) and tile.name != "floor":
                if self.rect.top <= tile.rect.bottom and self.rect.bottom > tile.rect.bottom:
                    print("collide top")
                    top = True

                if self.rect.bottom >= tile.rect.top and self.rect.top < tile.rect.top:
                    print("collide bottom")
                    bottom = True
                #pygame.draw.rect(screen, (0,255,0), self.rect)
   