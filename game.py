import pygame, sys, os
from pygame.locals import *
from settings import *
from player import Player
from enemy import Enemy
from weapon import *
from screen_profile import ScreenProfile
from gameover_screen import GameoverScreen
from random import choice, randint


def random_position():
    x = choice([randint(-100, -17), randint(window_size[0], window_size[0] + 100)])
    y = randint(window_size[1] - 120, window_size[1] - 70)
    return x, y


def create_enemies(length):
    enemies = []
    for enemy in range(length):
        x, y = random_position()
        enemies.append(Enemy(x, y, 17 * 2, 23 / 2, 3))
    return enemies


class Game:
    def __init__(self, window, clock, audio, font_25, font_40, font_80):
        self.window = window
        self.clock = clock
        self.running = True
        self.audio = audio
        self.player = Player(window_size[0] / 2 - 7, 50, 14 * 2, 26 / 2, 5)
        self.enemies = create_enemies(5)
        self.background_img = []
        self.background_frame = 0
        self.score = 0
        self.game_over = False
        self.font_25 = font_25
        self.font_40 = font_40
        self.font_80 = font_80
        self.guns_list = []
        self.can_armed = False
        self.screen_profile = ScreenProfile()
        self.gameover_screen = GameoverScreen(self.window, self.clock, self.font_40, self.font_80)

        for i in range(3):
            for j in range(40):
                self.background_img.append(pygame.transform.scale(pygame.image.load(os.path.join("assets/img", f"background_{i}.png")), (pygame.display.Info().current_w, pygame.display.Info().current_h)))

    def add_enemies(self):
        x, y = random_position()
        self.enemies.append(Enemy(x, y, 17 * 2, 23 / 2, 3))

    def get_score_label(self):
        return self.font_25.render(f"x{self.score}", 0, BLACK_COLOR)

    def run(self):
        self.audio.play_urban_ambience_sound(-1)

        while self.running:
            self.can_armed = False
            self.window.blit(self.background_img[self.background_frame], (0, 0))

            self.background_frame += 1
            if self.background_frame >= len(self.background_img):
                self.background_frame = 0

            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.player.is_armed:
                        self.player.shoot(self.audio)
                    else:
                        self.player.is_punching = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_f:
                        self.can_armed = True

            for index, enemy in enumerate(self.enemies):
                if enemy.rect.x < -100 or enemy.rect.x > window_size[0] + 100:
                    self.enemies.pop(index)
                    self.add_enemies()

                enemy.update()
                enemy.detect_bite(self.player, self.audio)
                enemy.take_damage(self.player)
                enemy.move()
                enemy.draw(self.window)

                # if enemy.rect.x <= self.player.rect.x <= enemy.rect.x + enemy.w:
                #     if self.player.rect.y > enemy.rect.y:
                #         enemy.draw(self.window)
                #         self.player.draw(self.window)
                #     elif self.player.rect.y < enemy.rect.y:
                #         self.player.draw(self.window)
                #         enemy.draw(self.window)

                if enemy.check_die():
                    spawn_random_weapon = randint(0, 10)
                    if spawn_random_weapon == 0:
                        self.guns_list.append({"ak-47": Ak47(enemy.rect.x, enemy.rect.y)})
                    elif spawn_random_weapon == 1:
                        self.guns_list.append({"glock": Glock(enemy.rect.y, enemy.rect.y)})

                    self.enemies.pop(index)
                    self.add_enemies()
                    self.audio.play_zombie_growing_sound()
                    self.score += 1

            if len(self.guns_list) > 0:
                for i, guns in enumerate(self.guns_list):
                    for gun in guns.items():
                        gun[1].update()
                        gun[1].draw(self.window)
                        if self.player.rect.colliderect(gun[1].rect) and self.can_armed:
                            self.audio.play_handgun_sound()
                            self.player.is_armed = True
                            self.player.gun_type = gun[0]
                            self.guns_list.pop(i)
                            self.can_armed = False

                        if gun[1].counter_invisible > 500:
                            self.guns_list.pop(i)

            self.player.update()
            self.player.bullet_update(self.window, self.enemies)
            self.player.move()
            self.player.draw(self.window)

            self.screen_profile.update(self.player)
            self.screen_profile.draw(self.window)

            if self.player.check_die():
                self.game_over = True

            if self.game_over:
                self.audio.stop_urban_ambience_sound()
                self.gameover_screen.run()
                self.running = False

            pygame.display.flip()
            self.clock.tick(fps)

    def draw(self):
        zombie_img = pygame.image.load(os.path.join("assets/img/enemy", "run_1.png"))
        zombie_img.set_colorkey(WHITE_COLOR)

        self.window.blit(self.get_score_label(), (window_size[0] - self.get_score_label().get_width() - 10, 10))
        self.window.blit(zombie_img, (window_size[0] - self.get_score_label().get_width() - 30, 5))
