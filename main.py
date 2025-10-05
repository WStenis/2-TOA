import pygame as pg
from screens.menu_screen import MenuScreen
from settings import *

pg.init()

screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption("Modular Game Framework")
clock = pg.time.Clock()

current_screen = MenuScreen()  # Start in menu

running = True
while running:
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False

    next_screen = current_screen.handle_events(events)
    current_screen.update()
    current_screen.draw(screen)

    if next_screen is not None:
        current_screen = next_screen  # Switch screen

    pg.display.flip()
    clock.tick(FPS)

pg.quit()
