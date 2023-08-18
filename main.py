import sys
from settings import *
import pygame as pg


class App:
    def __init__(self):
        pg.init()
        pg.display.set_caption('Brawler')
        self.screen = pg.display.set_mode(FIELD_RES)
        self.clock = pg.time.Clock()
        # background image
        self.bg_image = pg.image.load('assets/images/background/background.jpg').convert_alpha()

    def update(self):
        self.clock.tick(FPS)
        pg.display.update()

    def draw_bg(self):
        scaled_bg = pg.transform.scale(self.bg_image, FIELD_RES)
        self.screen.blit(scaled_bg, (0, 0))

    def draw(self):
        self.draw_bg()

    def reset(self):
        pass

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def run(self):
        while True:
            self.draw()
            self.check_events()
            self.update()


if __name__ == "__main__":
    app = App()
    app.run()
