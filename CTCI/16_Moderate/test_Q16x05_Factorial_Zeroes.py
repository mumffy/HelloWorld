from unittest import TestCase
from Q16x05_Factorial_Zeroes import countTrailingZeroes

class TestCountTrailingZeroes(TestCase):
    def test_invalid_input(self):
        self.assertEqual(countTrailingZeroes(0), -1)
        self.assertEqual(countTrailingZeroes(-1), -1)
        self.assertEqual(countTrailingZeroes(-123), -1)

    def test_baseline_inputs(self):
        self.assertEqual(countTrailingZeroes(1), 0)
        self.assertEqual(countTrailingZeroes(2), 0)
        self.assertEqual(countTrailingZeroes(4), 0)
        self.assertEqual(countTrailingZeroes(5), 1)

    def test_larger_factorials(self):
        pass