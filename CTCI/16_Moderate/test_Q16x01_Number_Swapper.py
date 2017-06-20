from unittest import TestCase


class TestNumberSwapper(TestCase):
    """
    because of how Python's parameter passing works, this problem cannot be tested in the conventional way of calling
        the method to perform the swap
    """

    def setUp(self):
        self._set_x_y(x=12, y=34)

    def _set_x_y(self, x, y):
        self.x = x
        self.y = y
        self._original_x = self.x
        self._original_y = self.y

    def _assert_x_y_swapped(self):
        self.assertEqual(self.x, self._original_y)
        self.assertEqual(self.y, self._original_x)

    # def test_swap_subtraction(self):
    #     self.x = self.x - self.y
    #     self.y = self.x - abs(self.x)
    #     self._assert_x_y_swapped()

    def test_swap_xor(self):
        self._set_x_y(x=12, y=34)
        self.x = self.x ^ self.y
        self.y = self.x ^ self.y  # original x
        self.x = self.x ^ self.y  # original y
        self._assert_x_y_swapped()

    def test_swap_xor_negative(self):
        self._set_x_y(x=-25, y=-44)
        self.x = self.x ^ self.y
        self.y = self.x ^ self.y  # original x
        self.x = self.x ^ self.y  # original y
        self._assert_x_y_swapped()

    def test_swap_xor_mixed_sign(self):
        self._set_x_y(x=57, y=-134)
        self.x = self.x ^ self.y
        self.y = self.x ^ self.y  # original x
        self.x = self.x ^ self.y  # original y
        self._assert_x_y_swapped()

    def test_swap_xor_failure(self):
        self._set_x_y(x=12, y=34)
        # no swapping attempted
        self.assertRaises(AssertionError, self._assert_x_y_swapped)
