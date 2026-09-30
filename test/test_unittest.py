import os
import sys
import unittest

# Get the path to the project's root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from src import calculator  # noqa: E402


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(2, 3), 5)
        self.assertEqual(calculator.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(2, 3), -1)
        self.assertEqual(calculator.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(2, 3), 6)
        self.assertEqual(calculator.multiply(5, 0), 0)

    def test_divide(self):
        self.assertEqual(calculator.divide(6, 3), 2)
        self.assertEqual(calculator.divide(7, 2), 3.5)

    def test_power(self):
        self.assertEqual(calculator.power(2, 3), 8)
        self.assertEqual(calculator.power(5, 0), 1)

    def test_average(self):
        self.assertEqual(calculator.average([1, 2, 3]), 2)
        self.assertEqual(calculator.average([1, 2]), 1.5)

    def test_errors(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(10, 0)
        with self.assertRaises(ValueError):
            calculator.average([])
        with self.assertRaises(ValueError):
            calculator.add("5", 2)


if __name__ == '__main__':
    unittest.main()
