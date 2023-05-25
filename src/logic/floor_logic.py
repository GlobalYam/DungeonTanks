# import random
import os
from random import randint

from data.process_data import read_room_data, read_room_data_from_dir, write_room_data
from logic.path_logic import PathManager

# INITIALIZE FLOOR


class GridManager:
    """Luokka, joka ylläpitää ohjelman hyödyntämää ruudukkoa, eli tasoa joka kuvaa tyrmän kerrosta.

    Attributes:
        my_grid: Luokan käyttämä ruudukko, tulevaisuudessa voisi olla useampia.
        grid_updated: Kertoo mikäli ruudukkoa on muutettu tällä askeleella
        grid_width:   Kertoo ruudukon leveyden
        grid_height:  Kertoo ruudukon korkeuden
        next_room_to_connect: Kertoo huoneen luvun jolle lisätään polut seuraavaksi
    """

    def __init__(self):
        """Luokan konstruktori, joka alustaa managerin."""
        self.my_grid: list[list[str]] = []
        self.grid_updated = True
        self.grid_width = 0
        self.grid_height = 0
        self.next_room_to_connect = 0

        self.loaded_floor = -1

        # door array used to store the door coordinates of each room.
        self.door_array = []

    def update(self):
        """Mikäli ruudukko viimeksi päivitettiin, aseta päivitys epätodeksi"""
        if self.grid_updated:
            self.grid_updated = False
            self.grid_width = len(self.my_grid[0])
            self.grid_height = len(self.my_grid)
            # print(self.my_grid)
            # print(self.door_array)
            return True
        return False

    def clear_floor(self, grid_width: int, grid_height: int):
        """Luo uuden, tyhjän kerroksen

        Args:
            grid_width:  uuden ruudukon leveys
            grid_height: uuden ruudukon korkeus
        """
        self.grid_updated = True
        self.door_array = []

        self.grid_width = grid_width
        self.grid_height = grid_height
        self.my_grid = []
        for y in range(self.grid_height):
            current_line = []
            for x in range(self.grid_width):
                if (
                    y == 0
                    or x == 0
                    or y == self.grid_height - 1
                    or x == self.grid_width - 1
                ):
                    current_line += "#"  # PERSONAL WALL
                elif (
                    y == 1
                    or x == 1
                    or y == self.grid_height - 2
                    or x == self.grid_width - 2
                ):
                    current_line += "="  # WALL AURA
                else:
                    current_line += "-"  # VOID
            self.my_grid.append(current_line)
            # print(''.join(current_line))
        return self.my_grid

    def create_floor(self, grid_width: int, grid_height: int, random_start=True):
        """Luo uuden, kerroksen satunnaisesti asetetuilla huoneilla

        Args:
            grid_width:   uuden ruudukon leveys
            grid_height:  uuden ruudukon korkeus
            random_start: määrittää tuleeko ensimmäisen huoneen olla
                          satunnaisesti asetettu, vai keskellä ruudukkoa
        """
        self.next_room_to_connect = 0
        self.grid_updated = True

        self.my_grid = self.clear_floor(grid_width, grid_height)

        starting_room = read_room_data(
            "src/data/room_presets/starting_rooms/starting_room.txt"
        )

        if random_start:
            x = randint(1, grid_width - 1)  # pylint: disable=invalid-name
            y = randint(1, grid_height - 1)  # pylint: disable=invalid-name

            fail_counter = 0
            fail_counter_max = 30

            while (
                self.place_room(self.my_grid, (x, y), starting_room) is False
                and fail_counter < fail_counter_max
            ):
                x = randint(1, grid_width)  # pylint: disable=invalid-name
                y = randint(1, grid_height)  # pylint: disable=invalid-name
                fail_counter += 1
        else:
            self.place_room(
                self.my_grid, (grid_width // 2, grid_height // 2), starting_room
            )

        fail_counter = 0
        fail_counter_max = 50

        for room in read_room_data_from_dir("src/data/room_presets/"):
            x = randint(1, grid_width - 1)  # pylint: disable=invalid-name
            y = randint(1, grid_height - 1)  # pylint: disable=invalid-name

            while (
                self.place_room(self.my_grid, (x, y), room) is False
                and fail_counter < fail_counter_max
            ):
                x = randint(1, grid_width)  # pylint: disable=invalid-name
                y = randint(1, grid_height)  # pylint: disable=invalid-name
                fail_counter += 1
        return self.my_grid

    def place_room(self, grid: list, coords: tuple, room: list, place_by_center=True):
        """Pyrkii asettamaan annetun huoneen ruudukkoon kordinaattien persteella

        Args:
            grid:  ruudukko johon asettaa huone
            rm_x:  huoneen x-kordinaatti
            rm_y:  huoneen y-kordinaatti
            room:  huone
            place_by_center: True: huone asetetaan keskipisteensä perusteella,
                             False: huone asetetaan vasemman yläkulman perusteella
        """
        rm_x, rm_y = coords
        self.grid_updated = True

        room = self.string_room_to_array_room(room)

        # grid_height = range(grid)
        # grid_width  = range(grid[0])

        room_height = len(room)
        room_width = len(room[0])

        if place_by_center:
            rm_x -= room_width // 2
            rm_y -= room_height // 2

        # check_if_free
        if not self.check_if_free(grid, (rm_x, rm_y), (room_height, room_width)):
            return False

        # place aura to grid
        for y in range(room_height + 2):  # pylint: disable=invalid-name
            for x in range(room_width + 2):  # pylint: disable=invalid-name
                grid[y + rm_y - 1][x + rm_x - 1] = "="
        # place tiles from room to grid

        # add new list to door_array
        self.door_array.append([])

        for y in range(room_height):  # pylint: disable=invalid-name
            for x in range(room_width):  # pylint: disable=invalid-name
                grid[y + rm_y][x + rm_x] = room[y][x]
                # check if the added tile is a door, if so, add door coordinates to door_array
                if room[y][x] == "D":
                    self.door_array[-1].append((x + rm_x, y + rm_y))

        return grid

    def check_if_free(
        self,
        grid: list,
        coords: tuple,
        room_size: tuple,
        exeptions=None,
    ):
        """Tarkistaa onko annettu neliö vapaana ruudukossa

        Args:
            grid:  ruudukko jota tarkistaa
            rm_x:  neliön/huoneen vasemman yläkulman x-kordinaatti
            rm_y:  neliön/huoneen vasemman yläkulman y-kordinaatti
            room_height: neliön/huoneen korkeus
            room_width:  neliön/huoneen leveys
            exeptions:   Mitkä merkit tulkitaan vapaaksi soluksi
        """
        rm_x, rm_y = coords
        room_height, room_width = room_size

        if exeptions is None:
            exeptions = [None]

        grid_height = len(grid)
        grid_width = len(grid[0])

        if (
            rm_x + room_width > grid_width
            or rm_y + room_height > grid_height
            or rm_x < 0
            or rm_y < 0
        ):
            return False
        for y in range(rm_y, rm_y + room_height):  # pylint: disable=invalid-name
            for x in range(rm_x, rm_x + room_width):  # pylint: disable=invalid-name
                cell = grid[y][x]
                if cell != "-" and not cell in exeptions:
                    return False
        return True

    def string_room_to_array_room(self, room: list):
        """Muuttaa listat merkkijonoja array muotoon, KEHITYS: voisi vaihtaa numpy array muotoon

        Args:
            room: kyseinen huone
        """
        for y in room:  # pylint: disable=invalid-name
            if isinstance(y, list):
                pass
            else:
                y.split()  # pylint: disable=invalid-name
        return room

    def room_to_string_room(self, room: list):
        """Muuttaa arrayt merkkijonolistoiksi
        Args:
            room: kyseinen huone
        """
        string = ""
        for y in room:  # pylint: disable=invalid-name
            line = []
            for x in y:
                line.append(x)

            line.append("\n")
            full_line = "".join(line)

            string = string + full_line

        return string

    def generate_paths(self):
        """Aloittaa prosessin, joka luo polkumanagerin, jolla luodaan polkuja huoneiden välillä"""
        if len(self.door_array) == 0:
            return

        if len(self.door_array) <= self.next_room_to_connect:
            self.next_room_to_connect = 0

        self.grid_updated = True
        my_path_manager = PathManager(self)
        list_of_coords = my_path_manager.generate_paths(self.next_room_to_connect)

        for coords in list_of_coords:
            # kaikki ympäröivät solut
            top_left = (coords[0] - 1, coords[1] - 1)  # x, y
            top_mid = (coords[0] - 1, coords[1])  # x, y
            top_right = (coords[0] - 1, coords[1] + 1)  # x, y

            mid_left = (coords[0], coords[1] - 1)  # x, y
            mid_mid = (coords[0], coords[1])  # x, y
            mid_right = (coords[0], coords[1] + 1)  # x, y

            bot_left = (coords[0] + 1, coords[1] - 1)  # x, y
            bot_mid = (coords[0] + 1, coords[1])  # x, y
            bot_right = (coords[0] + 1, coords[1] + 1)  # x, y

            surrounding_cels = [
                top_left,
                top_mid,
                top_right,
                mid_left,
                mid_mid,
                mid_right,
                bot_left,
                bot_mid,
                bot_right,
            ]

            for cell_to_seal in surrounding_cels:
                self.place_tile(self.my_grid, (cell_to_seal[0], cell_to_seal[1]), "#")
        self.next_room_to_connect += 1

    def place_tile(self, grid: list, tile_coords: tuple, tile: str, exeptions=None):
        """Metodi asettaa yhden solun annettuun ruudukon soluun,
            jos ruudukon solu on tyhjä, tai exeptions listaan kuuluva

        Args:
            grid: ruudukko johon lisätään
            t_x:  haluttu x-kordinaatti
            t_y:  haluttu y-kordinaatti
            tile: solu joka asettaa annettuun kohtaan
            exeptions: solut jotka saadaan korvata
        """
        t_x, t_y = tile_coords

        if exeptions is None:
            exeptions = ["="]
        self.grid_updated = True

        if not self.check_if_free(grid, (t_x, t_y), (1, 1), exeptions):
            return False

        grid[t_y][t_x] = tile
        return True

    def save_floor(self, path):
        """Metodi asettaa yhden solun annettuun ruudukon soluun,
            jos ruudukon solu on tyhjä, tai exeptions listaan kuuluva

        Args:
            path: ruudukko joka tallentaa
        """
        new_number = len(os.listdir(path))
        write_room_data(
            path,
            f"saved_floor_{new_number}.txt",
            self.room_to_string_room(self.my_grid),
        )

    def load_floor(self, path):
        """Metodi asettaa yhden solun annettuun ruudukon soluun,
            jos ruudukon solu on tyhjä, tai exeptions listaan kuuluva

        Args:
            path: ruudukko joka ladata
        """
        rooms_saved = len(os.listdir(path))

        self.loaded_floor += 1
        if self.loaded_floor >= rooms_saved:
            self.loaded_floor = 0

        self.my_grid = read_room_data_from_dir(path)[self.loaded_floor]
        print(f"floor loades: floor number: {self.loaded_floor}")
        self.door_array = []

        self.grid_updated = True
