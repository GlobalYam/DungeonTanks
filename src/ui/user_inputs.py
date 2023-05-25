import sys

import pygame as pg


def key_events(my_screen_manager, my_grid_manager):
    """Funktio joka kuuntelee käyttäjän näppäinpainalluksia,
    ja kutsuu managerien funktioita vastaavien toimintojen perusteella

    Args:
        my_screen_manager: Näyttömanageri, joka hoitaa näkymän ruudukkomanagerin perusteella.
        grid_manager:  Ruudukkomanageri, joka sisältää halutut metodit ruudukon muokkaamisen kannalta.
    """
    for event in pg.event.get():
        # QUIT
        if event.type == pg.QUIT:
            sys.exit()
        if event.type == pg.KEYDOWN:
            match event.key:
                case pg.K_q:
                    # QUIT
                    sys.exit()

                case pg.K_f:
                    # FULLSCREEN
                    my_screen_manager.toggle_fullsreen()

                case pg.K_s:
                    # SAVE
                    my_grid_manager.save_floor("src/data/local")

                case pg.K_l:
                    # LOAD
                    my_grid_manager.load_floor("src/data/local")

                case pg.K_p:
                    # PRINT ROOM
                    print(my_grid_manager.room_to_string_room(my_grid_manager.my_grid))

                case pg.K_u:
                    my_grid_manager.grid_updated = True

                case pg.K_r:
                    # RESET FLOOR
                    floor = my_grid_manager.create_floor(
                        my_grid_manager.grid_width, my_grid_manager.grid_height
                    )
                    for row_i, row in enumerate(floor):
                        my_grid_manager.my_grid[row_i] = row

                case pg.K_d:
                    # GENERATE DOORS
                    my_grid_manager.generate_paths()
                    print("generate paths")

                case pg.K_u:
                    # debug update
                    my_screen_manager.screen_update = True
