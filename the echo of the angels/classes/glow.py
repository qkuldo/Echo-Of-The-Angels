import pygame
class Glow:
    """A class to simulate light sources"""
    def __init__(self, center,dist,extension=20,light=200):
        self.extension = extension
        self.center = center
        self.dist = dist
        self.rect = pygame.Rect(self.center[0]-self.dist,self.center[1]-self.dist,self.dist,self.dist)
        self.rect.center = self.center
        self.outer_dist = self.dist+self.extension
        self.outer_rect = pygame.Rect(self.center[0]-self.outer_dist,self.center[1]-self.outer_dist,self.outer_dist,self.outer_dist)
        self.outer_rect.center = self.center
        self.timer = 500
        self.light = light
    def update(self,clock):
        self.timer -= clock.get_time()
        if (self.timer <= 0):
            if (self.rect.width == self.dist):
                self.rect.width = self.outer_dist
                self.rect.height = self.outer_dist
                self.outer_rect.width = self.outer_dist+self.extension
                self.outer_rect.height = self.outer_dist+self.extension
            else:
                self.rect.width = self.dist
                self.rect.height = self.dist
                self.outer_rect.width = self.outer_dist
                self.outer_rect.height = self.outer_dist
            self.outer_rect.center = self.center
            self.rect.center = self.center
            self.timer = 500
    def draw(self,screen):
        surf = pygame.Surface(self.rect.size).convert_alpha()
        surf.fill((220, 230, 0))
        surf.set_alpha(self.light)
        surf2 = pygame.Surface(self.outer_rect.size).convert_alpha()
        surf2.fill((0,90,90))
        surf2.set_alpha(self.light-20)
        screen.blit(surf2,self.outer_rect)
        screen.blit(surf,self.rect)