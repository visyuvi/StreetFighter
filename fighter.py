import pygame
from settings import *


class Fighter:
    def __init__(self, x, y, app):
        self.attacking = False
        self.attack_type = 0
        self.app = app
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0
        self.jump = False

    def move(self, target):
        SPEED = 10
        GRAVITY = 2
        dx = 0
        dy = 0

        # get key presses
        key = pygame.key.get_pressed()

        # can only perform other actions if not currently attacking
        if not self.attacking:
            # movement
            if key[pg.K_a]:
                dx = -SPEED
            if key[pg.K_d]:
                dx = SPEED

            # jump
            if key[pg.K_w] and not self.jump:
                self.vel_y = -30
                self.jump = True

            # attack
            if key[pg.K_r] or key[pg.K_t]:
                self.attack(target)
                # determine which attack type activated
                if key[pg.K_r]:
                    self.attack_type = 1
                if key[pg.K_t]:
                    self.attack_type = 2

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

    def attack(self, target):
        self.attacking = True
        attacking_rect = pygame.Rect(self.rect.centerx, self.rect.y,  2 * self.rect.width, self.rect.height)
        if attacking_rect.colliderect(target.rect):
            print("Hit")
        pg.draw.rect(self.app.screen, GREEN, attacking_rect)

    def draw(self):
        pg.draw.rect(self.app.screen, RED, self.rect)
