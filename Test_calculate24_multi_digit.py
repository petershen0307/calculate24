import unittest
from calculate24_multi_digit import *


class TestFind24MultiDigit(unittest.TestCase):
    def test_list_all_exponential_permutation(self):
        self.assertEqual(list_all_exponential_permutation(1, ['+', '-', '*', '/']), [['+', '-', '*', '/']])

    def test_list_all_factorial_permutation(self):
        self.assertEqual(list_all_factorial_permutation(['+']), [['+']])
        self.assertEqual(list_all_factorial_permutation([1]), [[1]])
        self.assertEqual(list_all_factorial_permutation([1, 2]), [[1, 2], [2, 1]])
        self.assertEqual(list_all_factorial_permutation([1, 2, 3]),
                         [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])
        self.assertEqual(list_all_factorial_permutation([1, 2, '3']),
                         [[1, 2, '3'], [1, '3', 2], [2, 1, '3'], [2, '3', 1], ['3', 1, 2], ['3', 2, 1]])
        self.assertEqual(list_all_factorial_permutation([11, 22, '3', '+']),
                         [[11, 22, '3', '+'], [11, 22, '+', '3'], [11, '3', 22, '+'],
                          [11, '3', '+', 22], [11, '+', 22, '3'], [11, '+', '3', 22],
                          [22, 11, '3', '+'], [22, 11, '+', '3'], [22, '3', 11, '+'],
                          [22, '3', '+', 11], [22, '+', 11, '3'], [22, '+', '3', 11],
                          ['3', 11, 22, '+'], ['3', 11, '+', 22], ['3', 22, 11, '+'],
                          ['3', 22, '+', 11], ['3', '+', 11, 22], ['3', '+', 22, 11],
                          ['+', 11, 22, '3'], ['+', 11, '3', 22], ['+', 22, 11, '3'],
                          ['+', 22, '3', 11], ['+', '3', 11, 22], ['+', '3', 22, 11]])
