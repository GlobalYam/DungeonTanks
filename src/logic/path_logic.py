class PathManager:
    """Luokka, joka vastaa polkujen lisäämisestä.

    Attributes:
        my_grid_manager: Luokan kutsunut ruudukkomanageri.
        grid_updated: Kertoo mikäli ruudukkoa on muutettu tällä askeleella, tällä hetkellä turha
        temp_grid:   Väliaikainen ruudukko, johon voidaan luoda polut
        room_num:  Huoneen lukunumero, joka yhdistää poluilla
    """

    def __init__(self, my_grid_manager):
        """Luokan konstruktori, joka alustaa managerin.

        Args:
            my_grid_manager:  Luokan kutsunut ruudukkomanageri.
        """
        self.my_grid_manager = my_grid_manager
        self.grid_updated = False
        self.temp_grid = False
        self.room_num = 0

    # def find_next(current_rooms, target_rooms):
    #     add current_rooms.doors to djikstra
    #     Modify djikstra to make turns more expensive
    #     "Terminate" on target_rooms.door
    #     Create path (possibly prettiest one)

    def generate_paths(self, room_to_generate_paths_for):
        """Luokan metodi joka luo polut

        Args:
            room_to_generate_paths_for:  Huoneen lukunumero, joka yhdistää poluilla.
        """
        # door array used to store the door coordinates of each room.
        # self.my_grid_manager.door_array.copy() #
        temp_doors = [line.copy() for line in self.my_grid_manager.door_array]

        room_doors = temp_doors[room_to_generate_paths_for]

        # self.my_grid_manager.my_grid.copy() #
        temp_grid = [line.copy() for line in self.my_grid_manager.my_grid]

        # make templist for the doors of a single room
        temp_paths = []

        # start paths for room
        for door_number, door in enumerate(room_doors):
            temp_paths.append([])

            if self.expand_branch(door, temp_grid, temp_paths[door_number]):
                print("two paths immidiately connected!")

        # print(f'temp_paths for current room: {temp_paths}')
        max_path_lenght = 1000
        for iter_num in range(0, max_path_lenght):
            lists_used = 4
            # print(f'handling branch repeat num: {iter_num}')
            for iterator, branch in enumerate(temp_paths):
                # print(f'branch_len, branh_num {len(branch), iterator}')
                lenght = len(branch)
                if lenght == 0:
                    lists_used -= 1
                    continue
                if lenght > iter_num:
                    if self.expand_branch(
                        branch[iter_num], temp_grid, temp_paths[iterator]
                    ):
                        temp_paths[iterator] = []
                        # print('found connection')

                        x_coord, y_coord = branch[iter_num]
                        next_coords = temp_grid[y_coord][x_coord]
                        list_of_path_coords = []
                        # print(f'x_coord, y_coord: {x_coord, y_coord}')
                        # print(f'next_coords: {next_coords}')
                        # print(branch)

                        self.my_grid_manager.my_grid[y_coord][x_coord] = "X"
                        list_of_path_coords.append((x_coord, y_coord))

                        for _ in range(iter_num):
                            self.my_grid_manager.my_grid[next_coords[1]][
                                next_coords[0]
                            ] = "X"

                            if temp_grid[next_coords[1]][next_coords[0]] == next_coords:
                                continue

                            list_of_path_coords.append(next_coords)
                            # print(next_coords)
                            next_coords = temp_grid[next_coords[1]][next_coords[0]]

                        return list_of_path_coords
            # print(lists_used)
            if lists_used <= 1:
                return []

        return []

    def expand_branch(self, path_parent, grid, temp_paths):
        """Metodi joka laajentaa haaraa yhdellä askeleella eteenpäin.

        Args:
            path_parent:  polku vanhempi, jota laajentaa.
            grid:  ruudukko johon lisätä uudet haarat
            temp_paths:  lista johon lisätään lisätyt solut

        """
        # print(path_parent)
        x, y = path_parent

        # print(f'y: {y}')
        # print(f'x: {x}')

        tile = grid[y][x]

        if tile == "D":
            grid[y][x] = (x, y)

        upper_tile = (x, y - 1)
        lower_tile = (x, y + 1)
        left_tile = (x - 1, y)
        right_tile = (x + 1, y)

        child_tiles = [upper_tile, lower_tile, left_tile, right_tile]

        for coords in child_tiles:
            tile = grid[coords[1]][coords[0]]
            if tile in ("-", "="):
                # checked tile is all good, now it can be set to my tile.
                grid[coords[1]][coords[0]] = path_parent
                temp_paths.append(coords)
            elif tile == "D":
                return True
        return False
