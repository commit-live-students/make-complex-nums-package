from __future__ import division
from unittest import TestCase
from build import complex_number
from math import sqrt, exp, pi
from math import sin, cos, atan


class TestComplex_number(TestCase):

    def test_argument(self):
        a = complex_number(3, 4)
        self.assertAlmostEqual(a.argument(), 0.9272952180016122)

    def test_abs(self):
        b = complex_number(0, -3)
        self.assertEqual(abs(b), 3.0)

    def test_operators(self):
        a = complex_number(3, 4)
        b = complex_number(0, -3)
        self.assertEqual(complex_number(9, 12), a*3)
        self.assertEqual(complex_number(3, 1), a+b)