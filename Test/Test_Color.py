import unittest
from Color import Color


class MyTestCase(unittest.TestCase):
    def test_print(self):
        c1 = Color(0, 0.2, 0.1)
        c1.print_color()
        self.assertEqual(True,True)

    def test_add_Color(self):
        c1 = Color(0, 0, 1)
        c2 = Color(0, 1, 0)
        c1.add_color(c2)
        self.assertEqual(0,c1.red)
        self.assertEqual(1,c1.green)
        self.assertEqual(1, c1.blue)

    def test_subtract_Color(self):
        c1 = Color(0, 0, 1)
        c2 = Color(0, 1, 0)
        c1.subtract_color(c2)
        self.assertEqual(0, c1.red)
        self.assertEqual(0, c1.green)
        self.assertEqual(1, c1.blue)


if __name__ == '__main__':
    unittest.main()
