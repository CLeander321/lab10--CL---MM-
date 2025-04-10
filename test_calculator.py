#https://github.com/CLeander321/lab10--CL---MM-.git
#Partner 1: Chloe Leander
#Partner 2: Maliha Mokamlel
import unittest
import math
from calculator import *

class TestCalculator(unittest.TestCase):

    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self): # 3 assertions
        with self.assertRaises(ZeroDivisionError):
            divide(0, 5)
            raise ZeroDivisionError
    # ##########################

    ######## Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertEqual((2* 3), 6)
        self.assertEqual((-2* 5), -10)
        self.assertEqual((-2* -4), 8)

    def test_divide(self):  # 3 assertions
        self.assertEqual((6/2), 3)
        self.assertEqual((-8/ 2), -4)
        self.assertEqual((-10/-5), 2)
        self.assertAlmostEqual((7/ 3), 2.3333333, places=6)
        with self.assertRaises(ZeroDivisionError):
            (10/ 0)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
     #    call division function inside, example:
        with self.assertRaises(ValueError):
              divide(5, 0)
    #     fill in code

    def test_logarithm(self): # 3 assertions
        self.assertEqual(math.log10(1000), 3)
        self.assertEqual(math.log(math.e), 1)
        self.assertEqual(math.log10(1), 0)
    #     fill in code

    def test_log_invalid_base(self): # 1 assertion
     #    use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            math.log10(-1)
    #     fill in code
    # ##########################

    ######## Partner 1
    def test_log_invalid_argument(self):  # 1 assertion

    # # call log function inside, example:
        with self.assertRaises(ValueError):
            math.log(0, 5)

    def test_hypotenuse(self):  # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertEqual(hypotenuse(4, 3), 5.0)

    def test_sqrt(self):  # 3 assertions

    # # Test for invalid argument, example:
        with self.assertRaises(ValueError):
            math.sqrt(-1)
    #     # Test basic function
        self.assertEqual(math.sqrt(25), 5)
        self.assertEqual(math.sqrt(16), 4)
    ##########################


# Do not touch this
if __name__ == "__main__":
    unittest.main()
