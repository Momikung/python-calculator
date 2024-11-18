import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(2, 2), 4)

    def test_substract(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(5, 1), 4)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 7), 21)  
        self.assertEqual(self.calc.multiply(4, 7), 28)

    def test_divide(self):
        self.assertEqual(self.calc.divide(5, 1),5)  
        self.assertEqual(self.calc.divide(3, 3), 1)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(3,2),1 )  
        self.assertEqual(self.calc.modulo(5, 2), 1)
    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()