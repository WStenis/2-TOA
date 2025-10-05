import pygame as pg

class Obstacle(pg.sprite.Sprite):
    def __init__(self, x, y, width, height, color=(120, 70, 20)):
        super().__init__()
        self.image = pg.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
