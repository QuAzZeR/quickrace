import pygame
import random
from pygame.locals import *
from gamelib import SimpleGame
from element import *
class QuickRace(SimpleGame):
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    GREEN = pygame.Color('green')
    
    def __init__(self):
        super(QuickRace, self).__init__('QuickRace', QuickRace.BLACK, window_size = (320,480))
        self.score = 1

    def init(self):
        super(QuickRace, self).init() 
        global enemies,player
        self.a=-10
        self.isover=False
        player = Player()
        enemies = []
        for i in range(500):
            enemies.append(Enemie(random.randint(0,1000)%3,self.a))
            self.a-=180
    def render(self,surface):
        player.render(surface)
        for e in enemies:
            e.render(surface)
        self.render_score(surface)

    def render_score(self,surface):
        self.score_image = self.font.render("Score: %.0f" % (self.score/100), 0 ,QuickRace.GREEN)
        surface.blit(self.score_image, (10,10) )

    def update(self):
        if self.is_key_pressed(K_LEFT):
            player.move_left()
        elif self.is_key_pressed(K_RIGHT):
            player.move_right()
        for e in enemies:
            if not self.isover:
                self.score += 1
                e.update()
            if player.get_rect().colliderect(e.get_rect()):
                self.isover=True
def main():
    game = QuickRace()
    game.run()
if __name__ == '__main__':
    main()
