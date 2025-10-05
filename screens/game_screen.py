import pygame as pg
import sys
from settings import *
import player
import hud
import enemy
import obstacle

class GameScreen:
    def __init__(self):
        # --- Game Objects ---
        self.p1 = player.Player()
        self.hud = hud.HUD(self.p1)
        self.enemies = pg.sprite.Group(enemy.Enemy(), enemy.Enemy())
        self.obstacles = pg.sprite.Group(
            obstacle.Obstacle(300, 200, 100, 40),
            obstacle.Obstacle(500, 350, 60, 120)
        )

        # --- Layout ---
        self.TOP_BAR_HEIGHT = 80
        self.BOTTOM_BAR_HEIGHT = 80
        self.GAME_AREA = pg.Rect(
            0, self.TOP_BAR_HEIGHT,
            WINDOW_WIDTH, WINDOW_HEIGHT - self.TOP_BAR_HEIGHT - self.BOTTOM_BAR_HEIGHT
        )

        # --- Misc ---
        self.enemy_counter = 0
        self.inventory_open = False
        self.inventory_items = ["Sword", "Shield", "Potion"]
        self.font = pg.font.SysFont(None, 30)

    def handle_events(self, events):
        for event in events:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_e:
                    self.inventory_open = not self.inventory_open  # toggle inventory
                if event.key == pg.K_ESCAPE:
                    import screens.menu_screen
                    return screens.menu_screen.MenuScreen()  # back to menu
        return None

    def update(self):
        if not self.inventory_open:
            self.p1.update()
            if self.enemy_counter == 10:
                self.enemies.update()
                self.enemy_counter = 0

            # --- Collisions ---
            if pg.sprite.spritecollide(self.p1, self.enemies, False):
                if self.p1.hp > 0:
                    self.p1.hp -= 1
                else:
                    print("DEAD")

            if pg.sprite.spritecollide(self.p1, self.obstacles, False):
                print("Hit obstacle!")
        self.enemy_counter += 1

    def draw(self, surface):
        surface.fill(WHITE)

        # --- Top bar ---
        pg.draw.rect(surface, DARK_GRAY, (0, 0, WINDOW_WIDTH, self.TOP_BAR_HEIGHT))
        surface.blit(self.font.render(f"HP: {self.p1.hp}", True, (255, 255, 255)), (20, 20))
        surface.blit(self.font.render(f"Enemies: {len(self.enemies)}", True, (255, 255, 255)), (200, 20))

        # --- Bottom bar ---
        pg.draw.rect(surface, DARK_GRAY, (0, WINDOW_HEIGHT - self.BOTTOM_BAR_HEIGHT, WINDOW_WIDTH, self.BOTTOM_BAR_HEIGHT))
        surface.blit(self.font.render("Press [E] to open inventory", True, (255, 255, 255)), (20, WINDOW_HEIGHT - 55))

        # --- Game area border ---
        pg.draw.rect(surface, BLACK, self.GAME_AREA, 2)

        # --- Draw entities ---
        self.obstacles.draw(surface)
        self.enemies.draw(surface)
        self.p1.draw(surface)
        self.hud.draw(surface)



        # --- Inventory overlay ---
        if self.inventory_open:
            self.draw_inventory(surface)

    def draw_inventory(self, surface):
        overlay = pg.Surface((WINDOW_WIDTH * 0.6, WINDOW_HEIGHT * 0.6))
        overlay.fill((50, 50, 50))
        overlay.set_alpha(220)
        rect = overlay.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        surface.blit(overlay, rect)

        title = self.font.render("INVENTORY", True, (255, 255, 0))
        surface.blit(title, (rect.x + 20, rect.y + 20))
        for i, item in enumerate(self.inventory_items):
            text = self.font.render(f"- {item}", True, (255, 255, 255))
            surface.blit(text, (rect.x + 40, rect.y + 70 + i * 30))
