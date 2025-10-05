import pygame as pg
from pygame.locals import *
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("sprites/player.png").convert_alpha()
        self.rect = self.image.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        self.hp = 50
        self.speed = 5

    def update(self):
        pressed = pg.key.get_pressed()
        dx, dy = 0, 0

        if pressed[K_a] and self.rect.left > 0:
            dx = -self.speed
        if pressed[K_d] and self.rect.right < WINDOW_WIDTH:
            dx = self.speed
        if pressed[K_w] and self.rect.top > GAME_TOP:
            dy = -self.speed
        if pressed[K_s] and self.rect.bottom < GAME_BOTTOM:
            dy = self.speed

        self.rect.move_ip(dx, dy)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class HUD:
    def __init__(self, player):
        self.player = player
        self.font = pg.font.SysFont(None, 30)

    def draw(self, surface):
        # You can overlay this on top of the HUD image if you have one
        hp_text = self.font.render(f"HP: {self.player.hp}", True, (255, 255, 255))
        surface.blit(hp_text, (20, 20))

