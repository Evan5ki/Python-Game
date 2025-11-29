import pygame
import math
from background import screen, Width, Height
from globals import Loaded_Level, bullet_group, enemy_group
from bullet import Bullet

class Player:
    def __init__(self, speed, health, path):
        self.speed = speed
        self.health = health
        self.dx = 0
        self.dy = 0
        self.x = Width // 2
        self.y = Height // 2
        self.xaxis = 0
        self.yaxis = 0
        self.timer = 0
        self.angle = 0
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect(center=(Width // 2, Height // 2))
        self.rect2 = self.image.get_rect(center = (self.x, self.y))
        self.render = self.image

    def move(self, dt):
        """Does the calculation for player displacement and passes it out to levelbuilder via main"""
        keys = pygame.key.get_pressed()
        self.dy = 0
        self.dx = 0
        if keys[pygame.K_w]:
                if not w:
                    self.dy -= 1
        if keys[pygame.K_s]:
                if not s:
                    self.dy += 1
        if keys[pygame.K_a]:
                if not a:
                    self.dx -= 1
        if keys[pygame.K_d]:
                if not d:
                    self.dx += 1
        if self.dx != 0 or self.dy != 0: 
            length = math.sqrt(self.dx ** 2 + self.dy ** 2) 
            self.dx /= length
            self.dy /= length

        self.xaxis = self.dx * self.speed * dt
        self.yaxis = self.dy * self.speed * dt

        self.x += self.xaxis
        self.y += self.yaxis
        return self.xaxis, self.yaxis

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
    
    def check_collision(self, player_vectors):

        collision = False
        global w,a,s,d
        w = False
        a = False
        s = False
        d = False
        for tile in Loaded_Level:
            if self.rect.colliderect(tile.rect) and tile.name != "floor":
                #self.x -= player_vectors[0]
                if self.rect.top <= tile.rect.bottom and self.rect.bottom > tile.rect.bottom:
                    self.y -= player_vectors[1]
                    collision = True
                    return collision
                if self.rect.bottom >= tile.rect.top and self.rect.top < tile.rect.top:
                    self.y -= player_vectors[1]
                    collision = True
                    return collision
                
        for enemy in enemy_group:
            if self.rect.colliderect(enemy.rect):
                self.health -= 50
                
                 
                    
        #if top or bottom and left or right:
           # return deltay, deltax

    def shoot(self):
        bullet = Bullet(self.angle)
        bullet_group.add(bullet)
        
