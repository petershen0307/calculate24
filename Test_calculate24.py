import unittest
from calculate24 import *


class TestFind24(unittest.TestCase):
    def test_exhaustion(self):
        self.assertEqual(exhaustion_exponential(2, '12'), ['11', '12', '21', '22'])

    def test_exhaustion_factorial(self):
        self.assertEqual(exhaustion_factorial('1'), ['1'])
        self.assertEqual(exhaustion_factorial('12'), ['12', '21'])
        self.assertEqual(exhaustion_factorial('123'), ['123', '132', '213', '231', '312', '321'])

    def test_removed_duplicate_string(self):
        self.assertEqual(removed_duplicate_string(['1123', '1231']), ['1123'])
        self.assertEqual(removed_duplicate_string(['/*/', '//*']), ['/*/'])
        self.assertEqual(removed_duplicate_string(['//*', '*//', '-*+', '+*-']), ['//*', '-*+'])

    def test_calculate_with_postfix_string(self):
        self.assertEqual(calculate_with_postfix_string('12+'), 3)
        self.assertEqual(calculate_with_postfix_string('1+2'), None)
        self.assertEqual(calculate_with_postfix_string('12+3*'), 9)
        self.assertEqual(calculate_with_postfix_string('12+3*4/'), Fraction(9, 4))
        self.assertEqual(calculate_with_postfix_string('12+34*'), None)
        self.assertEqual(calculate_with_postfix_string('34*12+32-//'), 4)
