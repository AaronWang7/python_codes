# Sounds
import pygame
from pygame import mixer

# First BGM


def bgm_1():
    mixer.music.load("music\\relax_music.wav")
    mixer.music.play(-1)

# Second BGM


def bgm_2():
    mixer.music.load(
        "music\\Suspenseful.wav")
    mixer.music.play(-1)
