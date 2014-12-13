import pygame
from pygame.locals import *

class Player(object):
    
    def __init__(self, width=60, height=60, x=126, y=400,color=pygame.Color('blue')):
        self.color = color
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.vx = 5

    def render(self, surface):
        pygame.draw.rect(surface,self.color,pygame.Rect(self.x,self.y,self.height,self.width))
    
    def move_left(self):
        if self.x >= 20:
            self.x-=self.vx

    def move_right(self):
        if self.x <= 231:
            self.x+=self.vx

