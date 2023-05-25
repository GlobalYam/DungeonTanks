import os


def read_room_data(path):
    room_grid = []
    with open(path, encoding="utf-8") as file:
        for line in file:
            line = line.replace("\n", "")
            room_grid.append(line)
    return room_grid


def read_room_data_from_dir(path):
    return [
        read_room_data(f"{path}/{file}")
        for file in os.listdir(path)
        if file.endswith(".txt")
    ]


def write_room_data(path, name, grid):
    with open(f"{path}/{name}", "x", encoding="utf-8") as file:
        for line in grid:
            file.write(f"{line}")
    return file
