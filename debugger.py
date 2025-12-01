import pygame
from globals import debug_settings, Loaded_Level, bullet_group, enemy_group
from background import screen, Width, Height



def debug(clock, P1):
    if debug_settings:
        font = pygame.font.Font(None, 30)
        DXY_surface = font.render(f"DX: {round(P1.dx, 2)} DY: {round(P1.dy, 2)}", True, (255, 255, 255))
        DXY_rect = DXY_surface.get_rect(midleft=(Width*0.01, Height* 0.02))
        screen.blit(DXY_surface, DXY_rect)

        FPS_surface = font.render(f"Frames: {int(clock.get_fps())}", True, (255, 255, 255))
        FPS_rect = FPS_surface.get_rect(midright=(Width*0.99, Height* 0.02))
        screen.blit(FPS_surface, FPS_rect)
        
        XY_surface = font.render(f"X: {round(P1.x, 2)} Y: {round(P1.y, 2)}", True, (255, 255, 255))
        XY_rect = XY_surface.get_rect(topleft=(DXY_rect.bottomleft[0], DXY_rect.bottomleft[1]))
        screen.blit(XY_surface, XY_rect)
        
        Angle_surface = font.render(f"Angle {round(P1.angle, 2)}", True, (255, 255, 255))
        Angle_rect = Angle_surface.get_rect(topleft=(XY_rect.bottomleft[0], XY_rect.bottomleft[1]))
        screen.blit(Angle_surface, Angle_rect)
        
        for bullet in bullet_group:
            pygame.draw.rect(screen, (255,255,0), bullet.rect, 2)
        for enemy in enemy_group:
            pygame.draw.rect(screen, (255, 0, 255), enemy.rect, 2)
        for tile in Loaded_Level:
            pygame.draw.rect(screen, (255,0,0), tile.rect, 2)
        pygame.draw.rect(screen, (255,0,0), P1.rect, 2)
        pygame.draw.rect(screen, (0,0,255), P1.render_rect, 2)
        pygame.draw.circle(screen, (255, 0, 0), (Width//2, Height//2), 1)

