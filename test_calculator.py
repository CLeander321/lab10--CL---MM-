import unittest
import math
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(2, 3), 5)
    def test_divide_by_zero(self):
        self.assert(divide(15, 5), 3)
    def test_log_invalid_base(self):
        self.assertRaises(ValueError, logarithm, 0, 0)
    def test_logarithm(self):
        self.assertEqual(math.log10(1000), 3)
        self.assertEqual(math.log(math.e), 1)
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertEqual(math.multiply(2, 3), 6)
        self.assertEqual(math.multiply(-2, 5), -10)
        self.assertEqual(math.multiply(-2, -4), 8)

    def test_divide(self):  # 3 assertions
        self.assertEqual(math.divide(6, 2), 3)
        self.assertEqual(math.divide(-8, 2), -4)
        self.assertEqual(math.divide(-10, -5), 2)
        self.assertAlmostEqual(calculator.divide(7, 3), 2.3333333, places=6)
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(10, 0)

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_log_invalid_argument(self):  # 1 assertion

    # # call log function inside, example:
        with self.assertRaises(ValueError):
            math.log(0, 5)

    def test_hypotenuse(self):  # 3 assertions
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13.0)
        self.assertEqual(calculator.hypotenuse(4, 3), 5)

    def test_sqrt(self):  # 3 assertions

    # # Test for invalid argument, example:
        with self.assertRaises(ValueError):
            math.sqrt(-1)
    #     # Test basic function
        self.assertEqual(calculator.sqrt(25), 5)
        self.assertEqual(calculator.sqrt(16), 4)
    ##########################


# Do not touch this
if __name__ == "__main__":
    unittest.main()
