import pygame
from settings import *


class Entity:
    def __init__(self, x, y, w, h, speed, begin_act):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = pygame.Rect(x, y, w, h)
        self.life = 100
        self.life_rect = pygame.Rect(x, y, w, 4)
        self.action = begin_act
        self.animations_database = {}
        self.frame = 0
        self.flip = False
        self.velocity = [0, 0]
        self.speed = speed

    @staticmethod
    def animations(path, frame_length):
        db_animation = []
        for i in range(len(frame_length)):
            animation_dir = path + "_" + str(i) + ".png"
            animation_image = pygame.transform.scale2x(pygame.image.load(animation_dir))
            animation_image.set_colorkey(WHITE_COLOR)
            for frame in range(frame_length[i]):
                db_animation.append(animation_image)
        return db_animation

    def move_right(self):
        self.rect.x += self.velocity[0]

    def move_left(self):
        self.rect.x += self.velocity[0]

    def move_up(self):
        self.rect.y += self.velocity[1]

    def move_down(self):
        self.rect.y += self.velocity[1]

    def update(self):
        self.frame += 1
        if self.frame >= len(self.animations_database[self.action]):
            self.frame = 0

        self.life_rect.x = self.rect.x
        self.life_rect.y = self.rect.y - 26

    def damage(self, life_decrease):
        self.life -= life_decrease
        self.life_rect.width -= self.w / (100 / life_decrease)

    def check_die(self):
        if self.life <= 0:
            return True

    def draw(self, window):
        window.blit(pygame.transform.flip(self.animations_database[self.action][self.frame], self.flip, False), (self.rect.x, self.rect.y - 20))
