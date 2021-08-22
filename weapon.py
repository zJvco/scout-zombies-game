import pygame, os
from settings import *


class Weapon:
    def __init__(self, x, y, name):
        self.img = pygame.transform.scale2x(pygame.image.load(os.path.join(f"assets/img/weapons/{name}", f"{name}.png")))
        self.rect = pygame.Rect(x, y, self.img.get_width(), self.img.get_height())
        self.counter_invisible = 0

    def update(self):
        self.counter_invisible += 1

    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), self.rect)
        window.blit(self.img, (self.rect.x, self.rect.y))


class Ak47(Weapon):
    def __init__(self, x, y):
        super().__init__(x, y, "ak-47")

    def update(self):
        super().update()

    def draw(self, window):
        super().draw(window)


class Glock(Weapon):
    def __init__(self, x, y):
        super().__init__(x, y, "glock")

    def update(self):
        super().update()

    def draw(self, window):
        super().draw(window)