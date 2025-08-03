import unittest
from simple_calculator import SimpleCalculator

class Test(unittest.TestCase):
    def setUp(self):
        self.calculate = SimpleCalculator()
    
    def test_add(self):
        self.assertEqual(self.calculate.add(3, 5), 8)
        self.assertEqual(self.calculate.add(-2, 7), 5)
        self.assertEqual(self.calculate.add(0, 0), 0)
        
    def test_subtract(self):
        self.assertEqual(self.calculate.subtract(3, -6), 9)
        self.assertEqual(self.calculate.subtract(0, 0), 0)
        self.assertEqual(self.calculate.subtract(7, 3), 4)
        
    def test_multiply(self):
        self.assertEqual(self.calculate.multiply(3, 4), 12)
        self.assertEqual(self.calculate.multiply(7, 2), 14)
        self.assertEqual(self.calculate.multiply(3, 0), 0)
        
    def test_divide(self):
        self.assertEqual(self.calculate.divide(3, 1), 3)
        self.assertEqual(self.calculate.divide(18, 6), 3)
        self.assertEqual(self.calculate.divide(-3, 1), -3)

if __name__ == "__main__":
    unittest.main()
