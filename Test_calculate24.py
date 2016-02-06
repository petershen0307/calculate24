import unittest
from calculate24 import *


class TestFind24(unittest.TestCase):
    def test_exhaustion(self):
        self.assertEqual(exhaustion_exponential(2, '12'), ['11', '12', '21', '22'])
        self.assertEqual(exhaustion_exponential(2, [[1], [2]]), [[1, 1], [1, 2], [2, 1], [2, 2]])
        self.assertEqual(exhaustion_exponential(2, [[1], [2], [10]]),
                         [[1, 1], [1, 2], [1, 10], [2, 1], [2, 2], [2, 10], [10, 1], [10, 2], [10, 10]])
        self.assertEqual(exhaustion_exponential(3, [[1], [2]]),
                         [[1, 1, 1], [1, 1, 2], [1, 2, 1], [1, 2, 2], [2, 1, 1], [2, 1, 2], [2, 2, 1], [2, 2, 2]])

    def test_exhaustion_factorial(self):
        self.assertEqual(exhaustion_factorial('1'), ['1'])
        self.assertEqual(exhaustion_factorial('12'), ['12', '21'])
        self.assertEqual(exhaustion_factorial('123'), ['123', '132', '213', '231', '312', '321'])
        self.assertEqual(exhaustion_factorial_int_list([[1], [2]]), [[1, 2], [2, 1]])
        self.assertEqual(exhaustion_factorial_int_list([[18], [200]]), [[18, 200], [200, 18]])
        self.assertEqual(exhaustion_factorial_int_list([[1], [2], [30]]),
                         [[1, 2, 30], [1, 30, 2], [2, 1, 30], [2, 30, 1], [30, 1, 2], [30, 2, 1]])

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
        self.assertEqual(calculate_with_postfix_string([3, 4, '*', 1, 2, '+', 3, 2, '-', '/', '/']), 4)
        self.assertEqual(calculate_with_postfix_string([10, 999, '+']), 1009)

    def test_postfix_to_infix(self):
        self.assertRaises(ValueError, postfix_to_infix, '1+2')
        self.assertEqual(postfix_to_infix('12+'), '(1+2)')
        self.assertEqual(postfix_to_infix('12+3-4*5/'), '((((1+2)-3)*4)/5)')
        self.assertEqual(postfix_to_infix([1, 2, '+']), '(1+2)')
        self.assertEqual(postfix_to_infix([100, 34, '+']), '(100+34)')
