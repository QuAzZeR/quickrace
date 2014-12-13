import pygame
from pygame.locals import *
from gamelib import SimpleGame
from element import *
class QuickRace(SimpleGame):
    BLACK = pygame.Color('black')
    def __init__(self):
        super(QuickRace, self).__init__('QuickRace', QuickRace.BLACK, window_size = (320,480))
        self.player = Player()
        self.player4 = Player(y=340, color = pygame.Color('white'))
        self.player2 = Player(x=21, y=340, color=pygame.Color('red'))
        self.player3 = Player(x=236, y = 340, color=pygame.Color('yellow'))
    def init(self):
        super(QuickRace, self).init()
    
    def render(self,surface):
        self.player2.render(surface)
        self.player3.render(surface)
        self.player4.render(surface)
        self.player.render(surface)
    def update(self):
        if self.is_key_pressed(K_LEFT):
            self.player.move_left()
        elif self.is_key_pressed(K_RIGHT):
            self.player.move_right()

def main():
    game = QuickRace()
    game.run()
if __name__ == '__main__':
    main()
