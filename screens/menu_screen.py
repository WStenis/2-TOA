import pygame as pg
from screens.game_screen import GameScreen
from settings import *

class MenuScreen:
    def __init__(self):
        self.font = pg.font.SysFont(None, 60)
        self.small_font = pg.font.SysFont(None, 35)

    def handle_events(self, events):
        for event in events:
            if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                return GameScreen()  # Switch to game
        return None

    def update(self):
        pass

    def draw(self, surface):
        surface.fill(DARK_GRAY)
        title = self.font.render("My Game", True, (255, 255, 255))
        start_text = self.small_font.render("Press ENTER to Start", True, (200, 200, 200))
        surface.blit(title, (WINDOW_WIDTH // 2 - title.get_width() // 2, 200))
        surface.blit(start_text, (WINDOW_WIDTH // 2 - start_text.get_width() // 2, 350))
