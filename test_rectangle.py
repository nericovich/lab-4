import unittest
from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):

    def test_area_zero(self):
        self.assertEqual(area(10, 0), 0)

    def test_area_square(self):
        self.assertEqual(area(10, 10), 100)

    def test_area_rectangle(self):
        self.assertEqual(area(5, 8), 40)

    def test_area_float(self):
        self.assertAlmostEqual(area(2.5, 4.2), 10.5)

    def test_area_negative(self):
        with self.assertRaises(ValueError):
            area(-5, 10)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(10, 0), 20)

    def test_perimeter_square(self):
        self.assertEqual(perimeter(10, 10), 40)

    def test_perimeter_rectangle(self):
        self.assertEqual(perimeter(5, 8), 26)

    def test_perimeter_float(self):
        self.assertAlmostEqual(perimeter(2.5, 4.2), 13.4)

    def test_perimeter_negative(self):
        with self.assertRaises(ValueError):
            perimeter(5, -10)


if __name__ == "__main__":
    unittest.main()
