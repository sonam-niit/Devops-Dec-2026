import unittest
from calculator import add,sub 

class CalculatorTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,2),3)
        self.assertEqual(add(-1,1),0)

    def test_sub(self):
        self.assertEqual(sub(-1,2),-3)

#  python3 -m unittest (run all test files)
#  python3 -m unittest test_calc_unittest.py (to run single testfile)
