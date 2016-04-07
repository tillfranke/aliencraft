import unittest
from colors import Colors, color,rgb

class Test_colors(unittest.TestCase):
    def test_color_get(self):
        c = Colors.get("Fuchsia")
        self.assertEqual(c,0xFF00FF)
        self.assertEqual(Colors.get("no_such_color"),0xFF69B4)
        self.assertEqual(Colors.get("Black"),0x000000)
        self.assertEqual(Colors.get("White"),0xFFFFFF)
    def test_color(self):
        self.assertEqual(color("MidnightBlue"),0x191970)
    def test_rgb(self):
        self.assertEqual(rgb("MidnightBlue"),(25,112,112))
if __name__ == '__main__':
    unittest.main()
