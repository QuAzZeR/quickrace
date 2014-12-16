import pygame
from pygame.locals import *
from gamelib import SimpleGame
from element import *
class QuickRace(SimpleGame):
    BLACK = pygame.Color('black')
    
    def __init__(self):
        super(QuickRace, self).__init__('QuickRace', QuickRace.BLACK, window_size = (320,480))

    def init(self):
        super(QuickRace, self).init() 
        global enemies,player
        self.isover=False
        player = Player()
        enemies = [Enemie(1,-480),Enemie(2,-960),Enemie(3,-1000)]        

    def render(self,surface):
        player.render(surface)
        for e in enemies:
            e.render(surface)

    def update(self):
        if self.is_key_pressed(K_LEFT):
            player.move_left()
        elif self.is_key_pressed(K_RIGHT):
            player.move_right()
        for e in enemies:
            if not self.isover:
                e.update()
            if player.get_rect().colliderect(e.get_rect()):
                self.isover=True
def main():
    game = QuickRace()
    game.run()
if __name__ == '__main__':
    main()
