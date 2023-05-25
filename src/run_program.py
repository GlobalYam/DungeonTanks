# THIS PART OF THE PROGRAM IS CONCERNED WITH THE GENERATION OF A FLOOR

# import random
# import math
# import sys
import pygame as pg

from logic.floor_logic import GridManager

# from logic.floor_logic import place_room
from ui.gui.gui_manager import ScreenManager
from ui.user_inputs import key_events

# PYGAME INIT & SCREEN
pg.init()
SCREEN_W = (pg.display.Info().current_w) // 2
SCREEN_H = (pg.display.Info().current_h) // 2

# VARIABLES
GRID_WIDTH = 70
GRID_HEIGHT = 40
my_grid_manager = GridManager()
my_grid = my_grid_manager.create_floor(GRID_WIDTH, GRID_HEIGHT)

# PYGAME DRAW LOGIC
# create a screen_manager
my_screen_manager = ScreenManager(SCREEN_W, SCREEN_H, my_grid_manager)

# quick instructions
print("R - generate new floor")
print("F - fullscreen")
print("D - generate doors")
print("S - save")
print("L - load")
print("U - update")
print("P - print current grid")
print("Q - quit")

# PYGAME LOOP
while True:
    # update the screen
    my_screen_manager.draw_screen_from_grid(my_grid_manager)

    # manage events, needs access to some variables
    key_events(my_screen_manager, my_grid_manager)
