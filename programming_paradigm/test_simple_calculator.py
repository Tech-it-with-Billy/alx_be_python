import unittest
from simple_calculator import SimpleCalculator

class Test(unittest.TestCase):
    def setUp(self):
        self.calculate = SimpleCalculator()
    
    def test_addition(self):
        self.assertEqual(self.calculate.addition(3, 5), 8)
        self.assertEqual(self.calculate.addition(-2, 7), 5)
        self.assertEqual(self.calculate.addition(0, 0), 0)
        
    def test_subtraction(self):
        self.assertEqual(self.calculate.subtraction(3, -6), 9)
        self.assertEqual(self.calculate.subtraction(0, 0), 0)
        self.assertEqual(self.calculate.subtraction(7, 3), 4)
        
    def test_multiplication(self):
        self.assertEqual(self.calculate.multiplication(3, 4), 12)
        self.assertEqual(self.calculate.multiplication(7, 2), 14)
        self.assertEqual(self.calculate.multiplication(3, 0), 0)
        
    def test_division(self):
        self.assertEqual(self.calculate.division(3, 1), 3)
        self.assertEqual(self.calculate.division(18, 6), 3)
        self.assertEqual(self.calculate.division(-3, 1), -3)

if __name__ == "__main__":
    unittest.main()
