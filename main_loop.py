#!/usr/bin/env python
# coding=utf-8

import socket

import time
import pygame
from pygame.sprite import Group

import Config as cfg
from settings import Settings
from game_stats import GameStats
from button import Button
import game_functions as gf

PORT = int(cfg.server_connection().getPORT())              # Arbitrary non-privileged port

time_out = 0.1  # Delay refresh (1 = 1 sec)
turn_time = 0
age = 0

def run_game():
    # Initialize pygame, settings, and screen object.
    global turn_time
    global age

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
            # Make the Time button.
            turn_time = int(time.clock())
            # print 60 - turn_time
            # print int(turn_time)

            time_button = Button(FLTL_settings, screen, str(60 - turn_time))
            time_button.draw_button()
            pygame.display.flip()

        gf.update_screen(FLTL_settings, screen, stats, play_button)

        # Every 60 sec to send date server.
        if turn_time >= 60:
            sock = socket.socket()
            sock.connect(('localhost', PORT))  # Connection to server
            sock.sendall(str(age))

            Data = sock.recv(4096)

            print "Age: " + Data
            turn_time = int(time.clock())

            Data = int(Data)
            sock.close()

        time.sleep(time_out)

    print "The client disconnected"
    # return turn_time


if __name__ == "__main__":
    run_game()
