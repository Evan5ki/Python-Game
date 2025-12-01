import pygame
from background import screen

class Button:
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text
        self.font = pygame.font.Font(None, 50)
        self.width, self.height = self.font.size(self.text)
        self.rect = pygame.Rect(x, y, self.width + 10, self.height + 10)
        self.rect.center = (self.x, self.y)

    def update(self):
        pygame.draw.rect(screen, (255,255,255), self.rect)
        text_surf = self.font.render(self.text, True, (0,255,0))
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    return True