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
    
