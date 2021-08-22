import pygame, sys, os
from settings import *


class GameoverScreen:
    def __init__(self, window, clock, font_40, font_80):
        self.window = window
        self.clock = clock
        self.running = True
        self.option = ""
        self.current_button = 0
        self.change_color = 255
        self.font_40 = font_40
        self.font_80 = font_80
        self.restart_rect = pygame.Rect(window_size[0] / 2 - 100, window_size[1] / 2 - 30, 200, 60)
        self.exit_rect = pygame.Rect(window_size[0] / 2 - 100, window_size[1] / 2 + 60, 200, 60)
        self.gameover_label = self.font_80.render("GAME OVER", 0, WHITE_COLOR)
        self.background_img = pygame.transform.scale(pygame.image.load(os.path.join("assets/img", "background_0.png")), (pygame.display.Info().current_w, pygame.display.Info().current_h))

    def get_option(self):
        return self.option

    def update(self):
        self.change_color -= 2
        if self.change_color < 0:
            self.change_color = 0

    def run(self):
        while self.running:
            self.window.blit(self.background_img, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.current_button -= 1
                    elif event.key == pygame.K_DOWN:
                        self.current_button += 1

                    if event.key == pygame.K_RETURN:
                        if self.current_button == 0:
                            self.option = "restart"
                        elif self.current_button == 1:
                            self.option = "exit"
                        self.running = False

            if self.current_button < 0:
                self.current_button = 1
            elif self.current_button > 1:
                self.current_button = 0

            self.update()
            self.draw()

            pygame.display.flip()
            self.clock.tick(fps)

    def draw(self):
        self.window.blit(self.gameover_label, (window_size[0] / 2 - self.gameover_label.get_width() / 2, 120))

        if self.current_button == 0:
            restart_label = self.font_40.render("RESTART", 0, BLACK_COLOR)
            pygame.draw.rect(self.window, WHITE_COLOR, self.restart_rect, 0, 5)
            self.window.blit(restart_label, (self.restart_rect.x + (self.restart_rect.w / 2 - restart_label.get_width() / 2), self.restart_rect.y + (self.restart_rect.h / 2 - restart_label.get_height() / 2)))
        else:
            restart_label = self.font_40.render("RESTART", 0, WHITE_COLOR)
            pygame.draw.rect(self.window, WHITE_COLOR, self.restart_rect, 1, 5)
            self.window.blit(restart_label, (self.restart_rect.x + (self.restart_rect.w / 2 - restart_label.get_width() / 2), self.restart_rect.y + (self.restart_rect.h / 2 - restart_label.get_height() / 2)))

        if self.current_button == 1:
            exit_label = self.font_40.render("EXIT", 0, BLACK_COLOR)
            pygame.draw.rect(self.window, WHITE_COLOR, self.exit_rect, 0, 5)
            self.window.blit(exit_label, (self.restart_rect.x + (self.exit_rect.w / 2 - exit_label.get_width() / 2), self.exit_rect.y + (self.exit_rect.h / 2 - exit_label.get_height() / 2)))
        else:
            exit_label = self.font_40.render("EXIT", 0, WHITE_COLOR)
            pygame.draw.rect(self.window, WHITE_COLOR, self.exit_rect, 1, 5)
            self.window.blit(exit_label, (self.restart_rect.x + (self.exit_rect.w / 2 - exit_label.get_width() / 2), self.exit_rect.y + (self.exit_rect.h / 2 - exit_label.get_height() / 2)))
