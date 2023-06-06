import pygame
from pygame.locals import *

class Ground(pygame.sprite.Sprite):
    def __init__(self,xpos,width,height,screen_height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('imagens/base.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(width,height))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect[0] = xpos
        self.rect[1] = screen_height - height
    def update(self,game_speed):
        self.rect[0] -= game_speed