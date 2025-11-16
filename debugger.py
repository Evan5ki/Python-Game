import pygame
from globals import debug_settings, P1
from background import screen, Width, Height



def debug(clock):
    if debug_settings:
        font = pygame.font.Font(None, 30)
        DXY_surface = font.render(f"DX: {round(P1.dx, 2)} DY: {round(P1.dy, 2)}", True, (255, 255, 255))
        DXY_rect = DXY_surface.get_rect(midleft=(Width*0.01, Height* 0.02))
        screen.blit(DXY_surface, DXY_rect)

        FPS_surface = font.render(f"Frames: {int(clock.get_fps())}", True, (255, 255, 255))
        FPS_rect = FPS_surface.get_rect(midright=(Width*0.99, Height* 0.02))
        screen.blit(FPS_surface, FPS_rect)
        
        XY_surface = font.render(f"X: {round(P1.x, 2)} DY: {round(P1.y, 2)}", True, (255, 255, 255))
        XY_rect = XY_surface.get_rect(topleft=(DXY_rect.bottomleft[0], DXY_rect.bottomleft[1]))
        screen.blit(XY_surface, XY_rect)
        
        pygame.draw.rect(screen, (255,0,0), P1.rect, 2)
        pygame.draw.rect(screen, (0,0,255), P1.render_rect, 2)
        pygame.draw.circle(screen, (255, 0, 0), (Width//2, Height//2), 1)

