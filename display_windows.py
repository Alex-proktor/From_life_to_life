#!/usr/bin/env python
# coding=utf-8

import sys

import pygame
from pygame.sprite import Group

import Config as cfg
from settings import Settings
# from button import Button

class Display_windows():
    def __init__(self):
        pygame.init()
        self.FLTL_settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.FLTL_settings.screen_width, self.FLTL_settings.screen_height))
        pygame.display.set_caption("FLTL")

    def Main(self):

        def play_button():
            """Initialize button attributes."""
            screen_rect = self.screen.get_rect()

            # Set the dimensions and properties of the button.
            width, height = 100, 50
            button_color = (245, 222, 179)
            text_color = (255, 255, 255)
            font = pygame.font.SysFont(None, 48)

            # Build the button's rect object, and center it.
            rect = pygame.Rect(0, 0, width, height)
            rect.center = screen_rect.center

            # The button message only needs to be prepped once.

            """Turn msg into a rendered image, and center text on the button."""
            msg_image = font.render("Play", True, text_color,
                                              button_color)
            msg_image_rect = msg_image.get_rect()
            msg_image_rect.center = rect.center

            # Draw the play button if the game is inactive.
            if cfg.check_events().getGameActive() == "False":
                self.screen.fill(button_color, rect)
                self.screen.blit(msg_image, msg_image_rect)

            return rect

        def check_events(rectpb):
            def check_play_button(rectpb, mouse_x, mouse_y):
                """Start a new game when the player clicks Play."""
                # rectpb = pygame.display.set_mode(
                #     (Settings().screen_width, Settings().screen_height))
                rectpb = pygame.Rect(rectpb)
                button_clicked = rectpb.collidepoint(mouse_x, mouse_y)

                if button_clicked and cfg.check_events().getGameActive() == "False":
                    # Change the status of the game.
                    cfg.check_events().setGameActive("True")
                    print "Game run!"

            """Respond to keypresses and mouse events."""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    cfg.check_events().setGameActive("False")
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    check_play_button(rectpb, mouse_x, mouse_y)

        rectpb = play_button()
        check_events(rectpb)

        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen, each pass through the loop.
        self.screen.fill(Settings().bg_color)

        # Make the Play button.
        play_button()


        # Make the most recently drawn screen visible.
        if cfg.check_events().getGameActive() == "False":
            pygame.display.flip()

    def InLife(self, turn_time):
        print "Run InLife!"
        # Make the Time button.
        def time_button(turn_time):
            """Initialize button attributes."""
            self.screen_rect = self.screen.get_rect()

            # Set the dimensions and properties of the button.
            self.width, self.height = 100, 50
            self.button_color = (0, 222, 179)
            self.text_color = (255, 255, 0)
            self.font = pygame.font.SysFont(None, 48)

            # Build the button's rect object, and center it.
            self.rect = pygame.Rect(0, 0, self.width, self.height)
            self.rect.center = self.screen_rect.center

            # The button message only needs to be prepped once.

            """Turn msg into a rendered image, and center text on the button."""
            self.msg_image = self.font.render("Time", True, self.text_color,
                                              self.button_color)
            self.msg_image_rect = self.msg_image.get_rect()
            self.msg_image_rect.center = self.rect.center

            # Draw the play button if the game is inactive.
            if cfg.check_events().getGameActive() == "False":
                self.screen.fill(self.button_color, self.rect)
                self.screen.blit(self.msg_image, self.msg_image_rect)

        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen, each pass through the loop.
        self.screen.fill(Settings().bg_color)

        # Make the Play button.
        time_button(str(turn_time))

        # Make the most recently drawn screen visible.
        if cfg.check_events().getGameActive() == "False":
            pygame.display.flip()
