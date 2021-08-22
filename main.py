import pygame, sys
from pygame.locals import *
from settings import *
from game import Game
from audio import Audio


class Main:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Scout Zombies")
        self.window = pygame.display.set_mode(window_size)
        self.clock = pygame.time.Clock()
        self.stage = "Game"
        self.font_40 = pygame.font.SysFont("comicsans", 40)
        self.font_80 = pygame.font.SysFont("comicsans", 80)
        self.font_25 = pygame.font.SysFont("comicsans", 25)
        self.audio = Audio()

    def update(self):
        game = Game(self.window, self.clock, self.audio, self.font_25, self.font_40, self.font_80)

        if self.stage == "Menu":
            pass
        elif self.stage == "Game":
            game.run()

            if game.gameover_screen.get_option() == "restart":
                self.stage = "Game"
            elif game.gameover_screen.get_option() == "exit":
                pygame.quit()
                sys.exit()
                # self.stage = "Menu"

    def run(self):
        while True:
            self.update()


if __name__ == "__main__":
    Main().run()
