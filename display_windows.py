#!/usr/bin/env python
# coding=utf-8

import pygame
from pygame.sprite import Group

from settings import Settings
from button import Button
import game_functions as gf


class Display_windows():
    def __init__(self):
        pygame.init()
        self.FLTL_settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.FLTL_settings.screen_width, self.FLTL_settings.screen_height))
        pygame.display.set_caption("FLTL")

    def Main(self):
        # Make the Play button.
        self.play_button = Button(self.screen, "Play")

    def InLife(self):
        # Make the Time button.
        self.time_button = Button(self.screen, "Play")
