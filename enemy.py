import pygame
from entity import Entity
from settings import *


class Enemy(Entity):
    def __init__(self, x, y, w, h, speed):
        super().__init__(x, y, w, h, speed, "run")
        self.animations_database = {"run": self.animations("assets/img/enemy/run", [7, 7, 7])}
        self.is_bite = False
        self.bite_timing = 0
        self.damage_timing = 0

        if x > 0:
            self.flip = True
        else:
            self.flip = False

    def move(self):
        self.velocity[0] = 0
        self.velocity[1] = 0

        if self.flip:
            self.velocity[0] -= self.speed
            super().move_left()
        else:
            self.velocity[0] += self.speed
            super().move_right()

    def detect_bite(self, player, audio):
        if not self.is_bite:
            if self.rect.colliderect(player.rect):
                self.is_bite = True
                player.damage(5)
                audio.play_zombie_attack_sound()
        else:
            self.bite_timing += 1
            if self.bite_timing >= 20:
                self.bite_timing = 0
                self.is_bite = False

    def take_damage(self, player):
        self.damage_timing += 1
        if player.rect.colliderect(self.rect) and player.is_punching:
            if self.damage_timing >= 20:
                self.damage(20)
                self.damage_timing = 0

    def update(self):
        super().update()

    def draw(self, window):
        super().draw(window)
        pygame.draw.rect(window, GREEN_COLOR, self.life_rect)
