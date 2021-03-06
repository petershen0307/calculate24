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
        self.assertEqual(calculate_with_postfix('12+'), 3)
        self.assertEqual(calculate_with_postfix('1+2'), None)
        self.assertEqual(calculate_with_postfix('12+3*'), 9)
        self.assertEqual(calculate_with_postfix('12+3*4/'), Fraction(9, 4))
        self.assertEqual(calculate_with_postfix('12+34*'), None)
        self.assertEqual(calculate_with_postfix('34*12+32-//'), 4)

    def test_calculate_with_postfix_int_str_list(self):
        self.assertEqual(calculate_with_postfix([11, 22, '+']), 33)
        self.assertEqual(calculate_with_postfix([1, '+', 2]), None)
        self.assertEqual(calculate_with_postfix([1, 2, '+', 3, '*']), 9)
        self.assertEqual(calculate_with_postfix([1, 2, '+', 3, '*', 4, '/']), Fraction(9, 4))
        self.assertEqual(calculate_with_postfix([1, 2, '+', 3, 4, '*']), None)
        self.assertEqual(calculate_with_postfix([3, 4, '*', 1, 2, '+', 3, 2, '-', '/', '/']), 4)

    def test_postfix_to_infix(self):
        self.assertRaises(ValueError, postfix_to_infix, '1+2')
        self.assertEqual(postfix_to_infix('12+'), '(1+2)')
        self.assertEqual(postfix_to_infix('12+3-4*5/'), '((((1+2)-3)*4)/5)')

    def test_postfix_to_infix_int_str_list(self):
        self.assertRaises(ValueError, postfix_to_infix, [1, '+', 2])
        self.assertEqual(postfix_to_infix([1, 2, '+']), '(1+2)')
        self.assertEqual(postfix_to_infix([1, 2, '+', 3, '-', 4, '*', 5, '/']), '((((1+2)-3)*4)/5)')
        self.assertEqual(postfix_to_infix([15, 23, '+']), '(15+23)')
