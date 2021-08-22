import pygame
from settings import *
from entity import Entity
from bullet import Bullet


class Player(Entity):
    def __init__(self, x, y, w, h, speed):
        super().__init__(x, y, w, h, speed, "idle")
        self.animations_database = {"idle": self.animations("assets/img/player/normal/idle", [10]),
                                    "run": self.animations("assets/img/player/normal/run", [10, 10, 10]),
                                    "idle_punch": self.animations("assets/img/player/normal/idle_punch", [5, 5, 5]),
                                    "run_punch": self.animations("assets/img/player/normal/run_punch", [5, 5, 5]),
                                    "ak-47_idle": self.animations("assets/img/player/gun/ak-47/idle", [10]),
                                    "ak-47_run": self.animations("assets/img/player/gun/ak-47/run", [10, 10, 10]),
                                    "glock_idle": self.animations("assets/img/player/gun/glock/idle", [10]),
                                    "glock_run": self.animations("assets/img/player/gun/glock/run", [10, 10, 10])}
        self.is_armed = False
        self.gun_type = "nothing"
        self.is_punching = False
        self.bullets = []

    def move(self):
        self.velocity[0] = 0
        self.velocity[1] = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.velocity[0] += self.speed
            super().move_right()
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.velocity[0] -= self.speed
            super().move_left()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.velocity[1] -= self.speed
            super().move_up()
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.velocity[1] += self.speed
            super().move_down()

    def change_action(self, idle_name, run_name):
        if self.velocity[0] == 0:
            self.action = idle_name
        elif self.velocity[0] > 0:
            self.action = run_name
            self.flip = False
        elif self.velocity[0] < 0:
            self.action = run_name
            self.flip = True

    def check_wall_collision(self):
        if self.rect.x > window_size[0] - self.animations_database[self.action][self.frame].get_width():
            self.rect.x = window_size[0] - self.animations_database[self.action][self.frame].get_width()
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.y > window_size[1] - 70:
            self.rect.y = window_size[1] - 70
        if self.rect.y < window_size[1] - 120:
            self.rect.y = window_size[1] - 120

    def punch(self):
        if self.is_punching:
            if self.velocity[0] == 0:
                if self.frame >= len(self.animations_database["idle_punch"]) - 1:
                    self.frame = 0
                    self.is_punching = False
                else:
                    self.action = "idle_punch"
            elif self.velocity[0] != 0:
                if self.frame >= len(self.animations_database["run_punch"]) - 1:
                    self.frame = 0
                    self.is_punching = False
                else:
                    self.action = "run_punch"

    def shoot(self, audio):
        damage = 0
        if self.gun_type == "ak-47":
            damage = 50
            audio.play_ak47_sound()
        elif self.gun_type == "glock":
            damage = 25
            audio.play_glock_sound()

        pos_x = 0
        pos_y = self.rect.y + 8
        if self.flip:
            pos_x = self.rect.x - 10
        else:
            pos_x = self.rect.x + self.animations_database[self.action][self.frame].get_width() + 10

        self.bullets.append(Bullet(pos_x, pos_y, 20, self.flip, damage))

    def bullet_update(self, window, enemies):
        for i, bullet in enumerate(self.bullets):
            bullet.update()
            bullet.draw(window)

            if bullet.rect.x > window_size[0] or bullet.rect.x < -bullet.img.get_width():
                self.bullets.pop(i)

            for enemie in enemies:
                if bullet.rect.colliderect(enemie.rect):
                    enemie.damage(bullet.damage)
                    if len(self.bullets) > 0:
                        self.bullets.pop(i)

    def update(self):
        if self.is_armed:
            if self.gun_type == "ak-47":
                self.change_action("ak-47_idle", "ak-47_run")
            elif self.gun_type == "glock":
                self.change_action("glock_idle", "glock_run")
        else:
            self.change_action("idle", "run")

        self.punch()
        super().update()
        self.check_wall_collision()

    def draw(self, window):
        super().draw(window)
