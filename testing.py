import unittest
import main


class MyTestCase(unittest.TestCase):
    def test_point(self):
        line = [[1, -1], [1, 1]]
        x , y = line
        val = main.distance_between_point_and_line(x, y)
        self.assertEqual(val, None)  # add assertion here


if __name__ == '__main__':
    unittest.main()
