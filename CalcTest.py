import unittest
from Calc import Calculator  # The class we are going to implement

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        result = calc.add(2, 3)
        self.assertEqual(result, 5)  # Expect 2 + 3 = 5

    def test_subtract(self):
        calc = Calculator()
        result = calc.subtract(5, 3)
        self.assertEqual(result, 2)
        self.assertEqual(calc.subtract(3, 5), -2)
        self.assertEqual(calc.subtract(0, 0), 0)
        self.assertEqual(calc.subtract(3, -1), 4)
        self.assertEqual(calc.subtract(-1, -1), 0)
    def test_multiply(self):
        calc = Calculator()
        self.assertEqual(calc.multiply(2, 3), 6)
        self.assertEqual(calc.multiply(-2, 3), -6)
        self.assertEqual(calc.multiply(-2, -3), 6)
        self.assertEqual(calc.multiply(0, 3), 0)
    def test_divide(self):
        calc = Calculator()
        # Positive / positive
        self.assertEqual(calc.divide(6, 3), 2.0)
        # Non-exact division: specifies floating-point division
        self.assertEqual(calc.divide(5, 2), 2.5)
        self.assertIsInstance(calc.divide(5, 2), float)
        # Negative / positive
        self.assertEqual(calc.divide(-6, 3), -2.0)
        # Positive / negative
        self.assertEqual(calc.divide(6, -3), -2.0)
        # Negative / negative
        self.assertEqual(calc.divide(-6, -3), 2.0)
        
    def test_divide_by_zero(self):
        calc = Calculator()
        with self.assertRaises(ValueError):
            calc.divide(5, 0)

if __name__ == "__main__":
    unittest.main()