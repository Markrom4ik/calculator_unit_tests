import unittest

from calculator import add, subtract, multiply, divide


class CalculatorTestCase(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_subtract(self):
        self.assertEqual(subtract(7, 4), 3)

    def test_subtract_result_is_negative(self):
        self.assertEqual(subtract(3, 8), -5)

    def test_multiply(self):
        self.assertEqual(multiply(4, 5), 20)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(10, 0), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_with_remainder(self):
        self.assertEqual(divide(7, 2), 3.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)


if __name__ == "__main__":
    unittest.main()
