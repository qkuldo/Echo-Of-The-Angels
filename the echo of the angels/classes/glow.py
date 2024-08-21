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
        self.light = pygame.math.clamp(light,0,220)
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
        self.surf = pygame.Surface((self.outer_dist*2,self.outer_dist*2), pygame.SRCALPHA)
        self.layers = 3
        for i in range(self.layers):
            k = i*self.light
            k = pygame.math.clamp(k,0,255)
            pygame.draw.circle(self.surf,(k,k,k/1.6), self.surf.get_rect().center, self.outer_dist-i * 3)
        self.surf.set_alpha(self.light)
        screen.blit(self.surf,(self.outer_rect.x,self.outer_rect.y), special_flags=pygame.BLEND_RGBA_MAX)