import unittest
from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):

    def test_area_right(self):
        self.assertAlmostEqual(area(3, 4, 5), 6)

    def test_area_equilateral(self):
        self.assertAlmostEqual(area(2, 2, 2), 1.7320508075688772)

    def test_area_isosceles(self):
        self.assertAlmostEqual(area(5, 5, 6), 12)

    def test_perimeter_right(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_perimeter_equilateral(self):
        self.assertEqual(perimeter(5, 5, 5), 15)

    def test_perimeter_float(self):
        self.assertAlmostEqual(perimeter(2.5, 3.5, 4), 10)

    def test_area_zero(self):
        with self.assertRaises(ValueError):
            area(0, 4, 5)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area(-3, 4, 5)

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            area(1, 2, 10)

    def test_degenerate_triangle(self):
        with self.assertRaises(ValueError):
            perimeter(1, 2, 3)


if __name__ == "__main__":
    unittest.main()
