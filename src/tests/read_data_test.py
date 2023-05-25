import os
import unittest

from data.process_data import read_room_data_from_dir


class TestReadRoomDataFromDir(unittest.TestCase):
    def setUp(self):
        pass

    def test_path(self):
        path = os.path.join(
            os.path.dirname(__file__), "..", "data", "room_presets", "starting_rooms/"
        )
        room_to_read = read_room_data_from_dir(path)

        print(room_to_read)

        self.assertEqual(room_to_read, [["##D##", "#...#", "D.^.D", "#...#", "##D##"]])
