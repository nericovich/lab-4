import unittest
import math
from circle import area, perimeter


class CircleTestCase(unittest.TestCase):

    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_one(self):
        self.assertAlmostEqual(area(1), math.pi)

    def test_area_five(self):
        self.assertAlmostEqual(area(5), 25 * math.pi)

    def test_area_float(self):
        self.assertAlmostEqual(area(2.5), 6.25 * math.pi)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_one(self):
        self.assertAlmostEqual(perimeter(1), 2 * math.pi)

    def test_perimeter_five(self):
        self.assertAlmostEqual(perimeter(5), 10 * math.pi)

    def test_perimeter_float(self):
        self.assertAlmostEqual(perimeter(2.5), 5 * math.pi)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area(-5)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            perimeter(-1)


if __name__ == "__main__":
    unittest.main()
