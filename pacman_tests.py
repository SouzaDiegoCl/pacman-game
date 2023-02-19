import unittest
from pacman import find_pacman, move_pacman, play, next_position, within_borders
from ui import ui_print


class PacmanTest(unittest.TestCase):

    def test_find_pacman(self):
        map = [
            "|----------|",
            "|G..|..G...|",
            "|...PP.....|",
            "|.G.....|..|",
            "|........@.|",
            "|----------|"
        ]


        x, y = find_pacman(map)

        self.assertEqual(x, 4)
        self.assertEqual(y, 9)


    def test_find_pacman_when_doesnt_exist(self):
            map = [
                "|----------|",
                "|G..|..G..|",
                "|...PP.....|",
                "|.G....|..|",
                "|..........|",
                "|----------|"
            ]

            x, y = find_pacman(map)

            self.assertEqual(x, -1)
            self.assertEqual(y, -1)

    def test_move_pacman(self):
            move_pacman(map, 4, 1)
            new_x, new_y = find_pacman(map)

            self.assertEqual(new_x, 4)
            self.assertEqual(new_y, 1)


    def test_next_position(self):
        map = [
            "|----------|",
            "|G..|..G...|",
            "|...PP.....|",
            "|.G....@|..|",
            "|..........|",
            "|----------|"
        ]
        ui_print(map)
        next_x, next_y = next_position(map, 'a')
        print("**************")
        ui_print(map)
        self.assertEqual(next_x, 3)
        self.assertEqual(next_y, 6)

        print("testeDown")
        next_x, next_y = next_position(map, 's')
        print("**************")
        ui_print(map)
        self.assertEqual(next_x, 4)
        self.assertEqual(next_y, 7)

        print("testeWrongKey")
        next_x, next_y = next_position(map, 'g')
        play(map, 'g')
        x, y = find_pacman(map)
        print("**************")
        ui_print(map)
        self.assertEqual(next_x, -1)
        self.assertEqual(next_y, -1)
        #won't move
        self.assertEqual(x, 3)
        self.assertEqual(y, 7)