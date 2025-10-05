# hud.py
import pygame as pg
from settings import *

class HUD:
    def __init__(self, player):
        self.player = player
        self.font = pg.font.SysFont(None, 30)

    def draw(self, surface):
        # Draw health bar
        bar_width = 200
        bar_height = 25
        x, y = 20, 20
        pg.draw.rect(surface, (255,0,0), (x, y, bar_width, bar_height))  # background
        current_width = int(bar_width * (self.player.hp / 50))
        pg.draw.rect(surface, (0,255,0), (x, y, current_width, bar_height))  # health
