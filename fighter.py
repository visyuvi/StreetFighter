import pygame
from settings import *


class Fighter:
    def __init__(self, x, y, app):
        self.app = app
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0
        self.jump = False

    def move(self):
        SPEED = 10
        GRAVITY = 2
        dx = 0
        dy = 0

        # get key presses
        key = pygame.key.get_pressed()

        # movement
        if key[pg.K_a]:
            dx = -SPEED
        if key[pg.K_d]:
            dx = SPEED

        # jump
        if key[pg.K_w] and not self.jump:
            self.vel_y = -30
            self.jump = True

        # apply gravity
        self.vel_y += GRAVITY
        dy += self.vel_y

        # ensure player stays on screen
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > FIELD_W:
            dx = FIELD_W - self.rect.right
        if self.rect.bottom + dy > FIELD_H - 110:
            self.vel_y = 0
            dy = FIELD_H - 110 - self.rect.bottom
            self.jump = False

        # update player position
        self.rect.x += dx
        self.rect.y += dy

    def draw(self):
        pg.draw.rect(self.app.screen, RED, self.rect)
