import pygame, os
from settings import *


class Bullet:
    def __init__(self, x, y, velx, direction, damage):
        self.x = x
        self.y = y
        self.velx = velx
        self.direction = direction
        self.damage = damage
        self.img = pygame.transform.scale(pygame.image.load(os.path.join("assets/img/weapons", "bullet.png")), (5, 2))
        self.rect = pygame.Rect(x, y, self.img.get_width(), self.img.get_height())

    def update(self):
        if self.direction:
            self.rect.x -= self.velx
        else:
            self.rect.x += self.velx

    def draw(self, window):
        window.blit(self.img, (self.rect.x, self.rect.y))