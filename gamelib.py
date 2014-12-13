import pygame
from pygame.locals import *

class SimpleGame(object):

    def __init__(self, title, background_color, window_size = (640,480), fps = 60):
        self.title = title
        self.fps = fps
        self.window_size = window_size
        self.background_color = background_color
        self.is_terminated = False    

    def __game_init(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption(self.title)
        self.font = pygame.font.SysFont("monospace", 20)
    
    def terminate(self):
        self.is_terminated = True

    def __handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.terminate()

    def is_key_pressed(self, key):
        key_pressed = pygame.key.get_pressed()
        if key < 0 or key >= len(key_pressed):
            return False
        return (key_pressed[key])
    def run(self):
        self.init()
        while not self.is_terminated:
            self.__handle_events()
            self.update()
            self.surface.fill(self.background_color)
            pygame.draw.line(self.surface, pygame.Color('white'), (101,0),(101,480),9)
            pygame.draw.line(self.surface, pygame.Color('white'), (211,0),(211,480),9)
            self.render(self.surface)
            pygame.display.update()
            self.clock.tick(self.fps)

    def init(self):
        self.__game_init()
    
    def render(self,surface):
        pass
    
    def update(self):
        pass
    
