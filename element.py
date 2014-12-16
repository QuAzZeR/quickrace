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
        self.rect = Rect(self.x,self.y,self.height,self.width)

    def render(self, surface):
        pygame.draw.rect(surface,self.color,pygame.Rect(self.x,self.y,self.height,self.width))
    
    def move_left(self):
        if self.x >= 20:
            self.x-=self.vx
    def get_rect(self):
        self.rect = Rect(self.x,self.y,self.height,self.width)
        return self.rect
    def move_right(self):
        if self.x <= 231:
            self.x+=self.vx

class Enemie(object):
    LEFT_LANE=26
    MIDDLE_LANE= 126 
    RIGHT_LANE= 236
    LEFT_COLOR=pygame.Color('red');
    MIDDLE_COLOR=pygame.Color('white');
    RIGHT_COLOR=pygame.Color('green');
    WIDTH=60
    HEIGHT=60
    def __init__(self, lane = 1, y = 0):
        self.width = Enemie.WIDTH
        self.height = Enemie.HEIGHT
        self.y = y
        if lane == 0:
            self.x = Enemie.LEFT_LANE
            self.color=Enemie.LEFT_COLOR
        elif lane == 1:
            self.x= Enemie.MIDDLE_LANE
            self.color=Enemie.MIDDLE_COLOR
        elif lane == 2:
            self.x = Enemie.RIGHT_LANE
            self.color = Enemie.RIGHT_COLOR
        self.rect = pygame.Rect(self.x,self.y,self.height,self.width)

    def render(self, surface):
        pygame.draw.rect(surface,self.color,pygame.Rect(self.x,self.y,self.height,self.width))
    
    def update(self):
        self.y+=6
        self.rect = pygame.Rect(self.x,self.y,self.height,self.width)

    def get_rect(self):
        return self.rect

