import sys

import pygame

from display_windows import Display_windows
import Config as cfg
from settings import Settings
# from button import Button

def check_keydown_events(event):
    """Respond to keypresses."""
    if event.key == pygame.K_q:
        sys.exit()
        
def check_events(DispWind):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cfg.check_events().setGameActive("False")
            sys.exit()
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             mouse_x, mouse_y = pygame.mouse.get_pos()
#             check_play_button(DispWind, mouse_x, mouse_y)
# #
# def check_play_button(DispWind, mouse_x, mouse_y):
#     """Start a new game when the player clicks Play."""
#     play_button = Button(DispWind, "Play")
#     button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
#
#     if button_clicked and cfg.check_events().getGameActive() == "False":
#         # Change the status of the game.
#         cfg.check_events().setGameActive("True")
#         print "Game run!"

def update_screen(FLTL_settings, screen, play_button):
    """Update images on the screen, and flip to the new screen."""
    # Redraw the screen, each pass through the loop.
    screen.fill(FLTL_settings.bg_color)

    # Draw the play button if the game is inactive.
    if cfg.check_events().getGameActive() == "False":
        play_button.draw_button()

    # Make the most recently drawn screen visible.
    if cfg.check_events().getGameActive() == "False":
        pygame.display.flip()
    
