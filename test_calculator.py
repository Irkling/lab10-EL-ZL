# https://github.com/Irkling/lab10-EL-ZL
# Partner 1: Erik Liddle
# Partner 2: Zhiheng Liu

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    #     fill in code
    # ##########################

    def test_multiply(self): # 3 assertions
        assert multiply(1, 2) == 2
        assert multiply(0, 10) == 0
        self.assertEqual(multiply( 1.5, 2), 1.5 * 2)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2, 10), 10 / 2)
        assert div(2, -10) == -5
        assert div(10, 2) == 0.2

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

    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            assert logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        assert hypotenuse(3,4) == 5
        self.assertEqual(hypotenuse(3,4), hypotenuse(4,3))



    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
        assert square_root(1) == 1
        self.assertEqual(square_root(4), math.sqrt(4))

# Do not touch this
if __name__ == "__main__":
    unittest.main()