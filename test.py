from unittest import TestCase, main
from calculator import calculator

class TestCalculator(TestCase):
    """
    Unittest
    ===============
    Unittest для проверки корректности calculator module.
    """
    def test_plus(self):
        self.assertEqual(calculator(2, 2, '+'), 4)
    def test_minus(self):
        self.assertEqual(calculator(6, 2, '-'), 4)
    def test_multi(self):
        self.assertEqual(calculator(3, 2, '*'), 6)
    def test_divide(self):
        self.assertEqual(calculator(10, 5, '/'), 2)
#   def test_divide(self):
#       self.assertEqual(calculator(a, 5, '/'), 2)
#    def test_divide(self):
#        self.assertEqual(calculator(7, 0, '/'), 0)


if __name__ == '__main__':
    main()