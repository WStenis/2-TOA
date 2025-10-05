import pygame as pg
from pygame.locals import *
from settings import *
import random


class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_load = pg.image.load("sprites/enemy.png").convert()
        self.image = pg.transform.scale(self.image_load, (10, 20))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 120)

    def update(self):
        movement = random.randint(0, 100)
        direction = random.randint(0, 3)
        if direction == 0:
            if self.rect.left > 0:
                self.rect.move_ip(-10, 0)
        if direction == 1:
            if self.rect.right < WINDOW_WIDTH:
                self.rect.move_ip(10, 0)
        if direction == 2:
            if self.rect.top > GAME_TOP:
                self.rect.move_ip(0, -10)
        if direction == 3:
            if self.rect.bottom < GAME_BOTTOM:
                self.rect.move_ip((0, 10))

    def draw(self, surface):
        surface.blit(self.image, self.rect)
