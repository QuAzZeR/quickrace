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
        enemies = [Enemie(0,-10),Enemie(0,-160),Enemie(2,-310),Enemie(2,-460),Enemie(1,-610),Enemie(0,-760),Enemie(2,-910),Enemie(1,-1060),Enemie(1,-1210),Enemie(1,-1360),Enemie(1,-1510),Enemie(2,-1660),Enemie(0,-1810),Enemie(1,-1960),Enemie(1,-2110),Enemie(0,-2260),Enemie(2,-2410),Enemie(1,-2560),Enemie(0,-2710),Enemie(0,-2860),Enemie(0,-3010),Enemie(2,-3160),Enemie(2,-3310),Enemie(1,-3460),Enemie(1,-3610),Enemie(1,-3760),Enemie(2,-3910),Enemie(0,-4060),Enemie(1,-4210),Enemie(0,-4360),Enemie(1,-4510),Enemie(1,-4660),Enemie(0,-4810),Enemie(0,-4960),Enemie(1,-5110),Enemie(1,-5260),Enemie(1,-5410),Enemie(1,-5560),Enemie(0,-5710),Enemie(1,-5860),Enemie(2,-6010),Enemie(1,-6160),Enemie(2,-6310),Enemie(2,-6460),Enemie(2,-6610),Enemie(1,-6760),Enemie(0,-6910),Enemie(1,-7060),Enemie(0,-7210),Enemie(2,-7360),Enemie(0,-7510),Enemie(2,-7660),Enemie(0,-7810),Enemie(2,-7960),Enemie(0,-8110),Enemie(1,-8260),Enemie(1,-8410),Enemie(1,-8560),Enemie(2,-8710),Enemie(0,-8860),Enemie(2,-9010),Enemie(0,-9160),Enemie(1,-9310),Enemie(0,-9460),Enemie(1,-9610),Enemie(1,-9760),Enemie(0,-9910),Enemie(1,-10060),Enemie(2,-10210),Enemie(2,-10360),Enemie(2,-10510),Enemie(2,-10660),Enemie(0,-10810),Enemie(0,-10960),Enemie(0,-11110),Enemie(0,-11260),Enemie(1,-11410),Enemie(1,-11560),Enemie(1,-11710),Enemie(1,-11860),Enemie(1,-12010),Enemie(1,-12160),Enemie(2,-12310),Enemie(0,-12460),Enemie(1,-12610),Enemie(1,-12760),Enemie(2,-12910),Enemie(0,-13060),Enemie(1,-13210),Enemie(1,-13360),Enemie(2,-13510),Enemie(2,-13660),Enemie(2,-13810),Enemie(1,-13960),Enemie(1,-14110),Enemie(0,-14260),Enemie(1,-14410),Enemie(1,-14560),Enemie(2,-14710),Enemie(0,-14860),Enemie(2,-15010),Enemie(0,-15160),Enemie(2,-15310),Enemie(2,-15460),Enemie(1,-15610),Enemie(1,-15760),Enemie(1,-15910),Enemie(2,-16060),Enemie(1,-16210),Enemie(2,-16360),Enemie(1,-16510),Enemie(0,-16660),Enemie(2,-16810),Enemie(1,-16960),Enemie(0,-17110),Enemie(2,-17260),Enemie(1,-17410),Enemie(1,-17560),Enemie(0,-17710),Enemie(1,-17860),Enemie(2,-18010),Enemie(2,-18160),Enemie(1,-18310),Enemie(1,-18460),Enemie(2,-18610),Enemie(0,-18760),Enemie(1,-18910),Enemie(1,-19060),Enemie(0,-19210),Enemie(2,-19360),Enemie(1,-19510),Enemie(0,-19660),Enemie(2,-19810),Enemie(0,-19960),Enemie(0,-20110),Enemie(0,-20260),Enemie(1,-20410),Enemie(1,-20560),Enemie(0,-20710),Enemie(1,-20860),Enemie(2,-21010),Enemie(0,-21160),Enemie(0,-21310),Enemie(0,-21460),Enemie(0,-21610),Enemie(2,-21760),Enemie(1,-21910),Enemie(1,-22060),Enemie(2,-22210),Enemie(0,-22360),Enemie(1,-22510),Enemie(1,-22660),Enemie(1,-22810),Enemie(0,-22960),Enemie(1,-23110),Enemie(1,-23260),Enemie(0,-23410),Enemie(2,-23560),Enemie(2,-23710),Enemie(0,-23860),Enemie(1,-24010),Enemie(1,-24160),Enemie(0,-24310),Enemie(2,-24460),Enemie(0,-24610),Enemie(1,-24760),Enemie(1,-24910),Enemie(1,-25060),Enemie(2,-25210),Enemie(2,-25360),Enemie(0,-25510),Enemie(0,-25660),Enemie(1,-25810),Enemie(2,-25960),Enemie(1,-26110),Enemie(1,-26260),Enemie(1,-26410),Enemie(0,-26560),Enemie(2,-26710),Enemie(2,-26860),Enemie(1,-27010),Enemie(1,-27160),Enemie(2,-27310),Enemie(2,-27460),Enemie(2,-27610),Enemie(2,-27760),Enemie(1,-27910),Enemie(2,-28060),Enemie(0,-28210),Enemie(0,-28360),Enemie(0,-28510),Enemie(2,-28660),Enemie(1,-28810),Enemie(1,-28960),Enemie(2,-29110),Enemie(2,-29260),Enemie(1,-29410),Enemie(0,-29560),Enemie(1,-29710),Enemie(0,-29860)]
    
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
