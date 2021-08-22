import os
from pygame import mixer


class Audio:
    def __init__(self):
        mixer.music.load(os.path.join("assets/music", "draft-monk-ambience.mp3"))
        self.ak_47_sound = mixer.Sound(os.path.join("assets/sound", "ak-47_shoot_sound.wav"))
        self.glock_sound = mixer.Sound(os.path.join("assets/sound", "glock_shoot_sound.wav"))
        self.punch_sound = mixer.Sound(os.path.join("assets/sound", "punch_sound.wav"))
        self.zombie_attack_sound = mixer.Sound(os.path.join("assets/sound", "zombie_attack_sound.mp3"))
        self.zombie_growing_sound = mixer.Sound(os.path.join("assets/sound", "zombie_growing_sound.mp3"))
        self.urban_ambience_sound = mixer.Sound(os.path.join("assets/sound", "urban_ambient_sound.wav"))
        self.handgun_click_sound = mixer.Sound(os.path.join("assets/sound", "handgun-click_sound.mp3"))

    @staticmethod
    def play_background_music(loop=0):
        mixer.music.play(loop)

    @staticmethod
    def stop_background_music():
        mixer.music.stop()

    @staticmethod
    def volume_control_music(value):
        mixer.music.set_volume(value)

    def volume_control_sound(self, value):
        pass

    def play_ak47_sound(self, loop=0):
        self.ak_47_sound.play(loop)

    def play_glock_sound(self, loop=0):
        self.glock_sound.play(loop)

    def play_punch_sound(self, loop=0):
        self.punch_sound.play(loop)

    def play_zombie_attack_sound(self, loop=0):
        self.zombie_attack_sound.play(loop)

    def play_zombie_growing_sound(self, loop=0):
        self.zombie_growing_sound.play(loop)

    def play_urban_ambience_sound(self, loop=0):
        self.urban_ambience_sound.play(loop)

    def stop_urban_ambience_sound(self):
        self.urban_ambience_sound.stop()

    def play_handgun_sound(self, loop=0):
        self.handgun_click_sound.play(loop)