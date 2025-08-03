import unittest
from simple_calculator import SimpleCalculator

class Test(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        self.assertEqual(self.calc.add(3, 5), 8)
        self.assertEqual(self.calc.add(-2, 7), 5)
        self.assertEqual(self.calc.add(0, 0), 0)
        
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(3, -6), 9)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(7, 3), 4)
        
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(7, 2), 14)
        self.assertEqual(self.calc.multiply(3, 0), 0)
        
    def test_division(self):
        self.assertEqual(self.calc.divide(3, 1), 3)
        self.assertEqual(self.calc.divide(18, 6), 3)
        self.assertEqual(self.calc.divide(-3, 1), -3)

if __name__ == "__main__":
    unittest.main()
