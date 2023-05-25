# import random
# import math
import pygame as pg


class ScreenManager:
    """Luokka, joka vastaa näytölle piirtämisestä.

    Attributes:
        self.screen_update: Kertoo mikäli näyttöä tulee päivittää, jos True, piirä näytölle
        screen_res_default: Oletusarvoinen ikkunan resoluutio
        screen_w:     Ikkunan leveys
        screen_h:     Ikkunan korkeus
        display_surf: Ikkunan taso
        fullscreen:   Boolean; kertoo ollaanko kokonäytön tilassa
        cell_size:    Yhden solun sivun koko, jokainen solu on täydellinen neliö
        x_offset:     Kuinka kaukana ruudukon vasemmalla olevin solu on ikkunan vasemmasta reunasta
        y_offset:     Kuinka kaukana ruudukon korkeimmalla olevin solu on ikkunan yläreunasta
    """

    def __init__(self, screen_w, screen_h, my_grid_manager):
        """Luokan konstruktori, joka alustaa managerin.

        Args:
            screen_w:  näytön määritetty leveys
            screen_h:  näytön määritetty korkeus
            my_grid_manager: Luokan kutsunut ruudukkomanageri
        """
        # screen_updates
        self.screen_update = True

        grid_width = my_grid_manager.grid_width
        grid_height = my_grid_manager.grid_height

        # fullscreen_offsets
        self.screen_res_default = (screen_w, screen_h)
        self.screen_res_current = self.screen_res_default

        screen_w, screen_h = self.screen_res_current

        self.display_surf = pg.display.set_mode((screen_w, screen_h))

        self.fullscreen = False

        # Check if cell cize is restricted by having to fit grid to width or height
        self.cell_size = screen_w // grid_width

        if (screen_h // grid_height) < (screen_w // grid_width):
            self.cell_size = screen_h // grid_height

        x_offset = (screen_w - (grid_width) * self.cell_size) // 2
        y_offset = (screen_h - (grid_height) * self.cell_size) // 2

        self.offsets = (x_offset, y_offset)

    def draw_screen_from_grid(self, grid_manager):
        """Metodi joka piirtää ikkunaan annetun ruudukon

        Args:
            grid_manager:  Ruudukkomanageri, jonka my_grid piirretään näytölle.
        """
        if grid_manager.update() or self.screen_update:
            print("screen_updated")
            self.display_surf.fill((0, 0, 0))

            self.screen_update = False
            grid = grid_manager.my_grid

            for y, row in enumerate(grid):
                for x, cell in enumerate(row):
                    # Figure out color
                    cell_color = (0, 0, 0)

                    match cell:
                        case "=":
                            cell_color = (30, 30, 30)
                        case "#":
                            cell_color = (100, 100, 100)
                        case "D":
                            cell_color = (80, 80, 80)
                        case ".":
                            cell_color = (80, 80, 80)
                        case "-":
                            cell_color = (5, 5, 5)
                        case "^":
                            cell_color = (220, 220, 220)
                        case _:
                            cell_color = (200, 200, 200)

                    self.draw_cell_to_screen(grid_manager, x, y, cell_color)

            for color_i, room_doors in enumerate(grid_manager.door_array):
                # get fun colors for each door
                color_i += 1
                color = (
                    (color_i * color_i * 225 * 7) % 255,
                    (color_i * color_i * 225 * 3) % 255,
                    (color_i * color_i * 225 * 9) % 255,
                )
                for door in room_doors:
                    self.draw_cell_to_screen(grid_manager, door[0], door[1], color)

            pg.display.flip()

    def draw_cell_to_screen(self, grid_manager, x, y, cell_color):
        """Metodi joka piirtää yhden ruudukon solun omalle näytölle

        Args:
            grid_manager:  Ruudukkomanageri, jonka solu piirretään näytölle.
            x: x-kordinaatti johon piirrettään (vastaa ruudukko kordinaatteja, ei näyttökordinaatteja)
            y: y-kordinaatti johon piirrettään (vastaa ruudukko kordinaatteja, ei näyttökordinaatteja)
            cell_color: haluttu väri jolla pirtää solua vastaava neliö
        """
        # fullscreen_offsets
        # x_fullscreen_offset = 0
        # y_fullscreen_offset = 0
        # if self.fullscreen:
        #     x_fullscreen_offset = screen_w//2
        #     y_fullscreen_offset = screen_h//2

        grid_width = grid_manager.grid_width
        grid_height = grid_manager.grid_height

        screen_w, screen_h = self.screen_res_current

        # Check if cell cize is restricted by having to fit grid to width or height
        self.cell_size = screen_w // grid_width

        if (screen_h // grid_height) < (screen_w // grid_width):
            self.cell_size = screen_h // grid_height

        x_offset = (screen_w - (grid_width) * self.cell_size) // 2
        y_offset = (screen_h - (grid_height) * self.cell_size) // 2

        x_1 = int(x * self.cell_size) + x_offset
        y_1 = int(y * self.cell_size) + y_offset

        x_2 = self.cell_size
        y_2 = self.cell_size
        pg.draw.rect(self.display_surf, cell_color, pg.Rect(x_1, y_1, x_2, y_2))

    def toggle_fullsreen(self):
        """Metodi joka vaihtaa kokonäytöntilaa"""
        self.screen_update = True
        if self.fullscreen is False:
            pg.display.set_mode((0, 0), pg.FULLSCREEN)
            self.screen_res_current = pg.display.get_window_size()
            self.fullscreen = True
        else:
            self.screen_res_current = self.screen_res_default
            self.display_surf = pg.display.set_mode(self.screen_res_current)
            self.fullscreen = False
