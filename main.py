import sys

import pygame.draw

from settings import *
import pygame as pg
from fighter import Fighter


class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Brawler')
        self.screen = pg.display.set_mode(FIELD_RES)
        self.clock = pg.time.Clock()
        self.fighter1 = Fighter(200, 300, self)
        self.fighter2 = Fighter(700, 310, self)

        # background image
        self.bg_image = pg.image.load('assets/images/background/background.jpg').convert_alpha()

    def update(self):
        self.clock.tick(FPS)
        self.fighter1.move(self.fighter2)
        pg.display.update()

        # self.fighter2.move()

    def draw_bg(self):
        scaled_bg = pg.transform.scale(self.bg_image, FIELD_RES)
        self.screen.blit(scaled_bg, (0, 0))

    def draw(self):
        self.draw_bg()
        self.fighter1.draw()
        self.fighter1.draw_health_bar(20, 20)
        self.fighter2.draw()
        self.fighter2.draw_health_bar(580, 20)

    def reset(self):
        pass

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == "__main__":
    app = App()
    app.run()
