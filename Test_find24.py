import unittest
from find24 import *


class TestFind24(unittest.TestCase):
    def test_exhaustion(self):
        self.assertEqual(exhaustion(2, '12'), ['11', '12', '21', '22'])

    def test_combine_to_expression(self):
        self.assertEqual(combine_to_expression('1234', '*-+'), '1*2-3+4')

    def test_generate_all_expressions(self):
        self.assertEqual(generate_all_expressions(exhaustion(2, '12'), exhaustion(1, '+')),
                         ['1+1', '1+2', '2+1', '2+2'])
