import unittest

from logic.floor_logic import GridManager


class TestGridManager(unittest.TestCase):
    def setUp(self):
        pass

    def test_min_floor(self):
        self.w = 1
        self.h = 1

        self.manager = GridManager()
        self.manager.clear_floor(self.w, self.h)

        self.floor = self.manager.my_grid

        self.assertEqual(self.manager.my_grid, [["#"]])

    def test_small_room(self):
        self.w = 5
        self.h = 5

        self.manager = GridManager()
        self.floor = self.manager.clear_floor(self.w, self.h)

        self.assertEqual(
            self.manager.my_grid,
            [
                ["#", "#", "#", "#", "#"],
                ["#", "=", "=", "=", "#"],
                ["#", "=", "-", "=", "#"],
                ["#", "=", "=", "=", "#"],
                ["#", "#", "#", "#", "#"],
            ],
        )

    def test_update(self):
        self.w = 5
        self.h = 5

        self.manager = GridManager()
        self.floor = self.manager.clear_floor(self.w, self.h)

        self.assertEqual(self.manager.update(), True)

    def test_no_update(self):
        self.w = 5
        self.h = 5

        self.manager = GridManager()
        self.floor = self.manager.clear_floor(self.w, self.h)

        self.manager.update()

        self.assertEqual(self.manager.update(), False)

    def test_6x6_room(self):
        self.w = 6
        self.h = 6

        self.manager = GridManager()
        self.floor = self.manager.clear_floor(self.w, self.h)

        self.assertEqual(
            self.manager.my_grid,
            [
                ["#", "#", "#", "#", "#", "#"],
                ["#", "=", "=", "=", "=", "#"],
                ["#", "=", "-", "-", "=", "#"],
                ["#", "=", "-", "-", "=", "#"],
                ["#", "=", "=", "=", "=", "#"],
                ["#", "#", "#", "#", "#", "#"],
            ],
        )

    def test_check_if_free(self):
        self.w = 20
        self.h = 20

        self.manager = GridManager()
        self.floor = self.manager.clear_floor(self.w, self.h)

        free = self.manager.check_if_free(self.manager.my_grid, (10, 10), (1, 1))

        self.assertEqual(free, True)

    def test_create_floor_no_room(self):
        w = 3  # 70
        h = 3  # 40
        my_grid_manager = GridManager()
        my_grid = my_grid_manager.create_floor(w, h)

        self.assertEqual([["#", "#", "#"], ["#", "=", "#"], ["#", "#", "#"]], my_grid)
