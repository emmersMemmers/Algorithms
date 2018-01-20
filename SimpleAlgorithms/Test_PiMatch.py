import unittest
from PiMatch import calc_pi_match

#example 1: 3149 is calculated as: (314 - 314 = 0) + (149 - 314 = -165)/2 = -82.5

#example 2: 357878 (357-314=43)+(578-314=264)+(787-314=473)+(878-314=564)/4 = 336

class Test_PiMatch(unittest.TestCase):
    def test_calc_pi_match_is_neg_82p5(self):
        expected = -82.5
        actual = calc_pi_match(3149)
        self.assertEqual(expected, actual)

    def test_calc_pi_match_is_336(self):
        expected = 336
        actual = calc_pi_match(357878)
        self.assertEqual(expected, actual)

    def test_calc_pi_match_is_0_for_2_digits(self):
        expected = 0
        actual = calc_pi_match(22)
        self.assertEqual(expected, actual)

    def test_calc_pi_match_is_0_for_value_314(self):
        expected = 0
        actual = calc_pi_match(314)
        self.assertEqual(expected, actual)

    def test_calc_pi_match_has_decimal(self):
        expected = 0
        actual = calc_pi_match(3.14)
        self.assertEqual(expected, actual)