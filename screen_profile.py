import pygame, os
from settings import *


class ScreenProfile:
    def __init__(self):
        self.img = pygame.transform.scale(pygame.image.load(os.path.join("assets/img/player", "profile_img.png")), (13*5, 11*5))
        self.img.set_colorkey(WHITE_COLOR)
        self.life_rect_total = pygame.Rect(window_size[0] / 2 - 50, self.img.get_height() + 18, 100, 8)
        self.life_rect_current = pygame.Rect(window_size[0] / 2 - 50, self.img.get_height() + 18, 100, 8)

    def update(self, player):
        self.life_rect_current.width = player.life

    def draw(self, window):
        window.blit(self.img, (window_size[0] / 2 - self.img.get_width() / 2, 10))
        pygame.draw.rect(window, RED_COLOR, self.life_rect_total)
        pygame.draw.rect(window, GREEN_COLOR, self.life_rect_current)
