#!/usr/bin/env python
# coding=utf-8

import socket

import time
# import pygame
# from pygame.sprite import Group
import wx


from display_windows import Display_windows
import Config as cfg
from settings import Settings
from button import Button
import game_functions as gf

PORT = int(cfg.server_connection().getPORT())              # Arbitrary non-privileged port

Sec_in_one_year = 10    # must be = 60, but to debug put less
time_out = 0.1  # Delay refresh (1 = 1 sec)
turn_time = 0
Data = 0


def run_game():
    # Initialize settings, and screen object.
    global turn_time
    global Data

    start_time = 0
    DispWind = Display_windows()


    # Start the main loop for the game.
    while True:
        print "Bla"
    #     screen = pygame.display.set_mode(
    #         (Settings().screen_width, Settings().screen_height))
    #     # next string get broken display in run game
    #     gf.check_events(screen)
    #
    #     if cfg.check_events().getGameActive() == "True":
    #         if start_time == 0:
    #             start_time = time.time()
    #
    #         # Make the Time button.
    #         turn_time = int(time.time() - start_time)
    #         # print 60 - turn_time
    #         print int(turn_time)
    #
    #         """
    #         Need add Time_Button
    #         """
    #         # time_button = Button(Settings(), DispWind.InLife(), str(60 - turn_time))
    #         # time_button.draw_button()
    #         pygame.display.flip()
    #
    #     gf.update_screen(Settings(), DispWind.screen, DispWind.play_button)
    #
    #     # Every 60 sec to send date server.
    #     if turn_time >= Sec_in_one_year:
    #         sock = socket.socket()
    #         sock.connect(('localhost', PORT))  # Connection to server
    #         sock.sendall(str(Data))
    #
    #         Data = sock.recv(1024)
    #
    #         print "Age: " + Data
    #         turn_time = int(time.clock())
    #
    #         Data = int(Data)
    #         start_time += Sec_in_one_year
    #         sock.close()
    #
        time.sleep(time_out)
        DispWind.MainLoop()


    print "The client disconnected"
    # return turn_time


if __name__ == "__main__":
    # run_game()
    app = wx.PySimpleApp()
    frame = run_game()
    frame.Show(True)
    app.MainLoop()

