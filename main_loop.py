#!/usr/bin/env python
# coding=utf-8

import time
import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
# from scoreboard import Scoreboard
from button import Button
# from ship import Ship
import game_functions as gf

time_out = 0.5  # Задержка обновления экрана
turn_time = 0

def run_game():
    # Initialize pygame, settings, and screen object.
    global turn_time
    pygame.init()
    FLTL_settings = Settings()
    screen = pygame.display.set_mode(
        (FLTL_settings.screen_width, FLTL_settings.screen_height))
    pygame.display.set_caption("FLTL")
    
    # Make the Play button.
    play_button = Button(FLTL_settings, screen, "Play")
    
    # Create an instance to store game statistics, and a scoreboard.
    stats = GameStats(FLTL_settings)
    # sb = Scoreboard(FLTL_settings, screen, stats)
    
    # Set the background color.
    bg_color = (230, 230, 230)
    
    # Make a ship, a group of bullets, and a group of aliens.
    # ship = Ship(FLTL_settings, screen)
    bullets = Group()
    aliens = Group()
    
    # Create the fleet of aliens.
    # gf.create_fleet(FLTL_settings, screen, ship, aliens)

    begin_time = time.time()

    # Start the main loop for the game.
    while True:
        gf.check_events(FLTL_settings, screen, stats, play_button)

        if stats.game_active:
            # pass
            # Make the Time button.
            turn_time = int(time.time() - begin_time)
            print 60 - turn_time

            time_button = Button(FLTL_settings, screen, str(60 - turn_time))
            time_button.draw_button()
            pygame.display.flip()
        #     # ship.update()
        #     gf.update_bullets(FLTL_settings, screen, stats, aliens,
        #         bullets)
        #     gf.update_aliens(FLTL_settings, screen, stats, aliens,
        #         bullets)

        gf.update_screen(FLTL_settings, screen, stats, play_button)
        time.sleep(time_out)
    return turn_time


if __name__ == "__main__":
    run_game()
