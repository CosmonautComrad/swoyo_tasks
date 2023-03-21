import unittest
from roman_numeral import roman_numerals_to_int


class MyTestCase(unittest.TestCase):
    def test_not_str(self):
        """Should return None if not a string was passed """
        self.assertEqual(roman_numerals_to_int(451), None)

    def test_not_roman(self):
        """Should return None if not roman symbols were passed"""
        self.assertEqual(roman_numerals_to_int("MMA"), None)

    def test_simple_roman(self):
        """Should return 500 which is in roman dictionary"""
        self.assertEqual(roman_numerals_to_int("D"), 500)

    def test_complex_roman_1(self):
        """Should return 3437 which needs to be calculated"""
        self.assertEqual(roman_numerals_to_int("MMMCDXXXVII"), 3437)

    def test_complex_roman_2(self):
        """Should return 9 which needs to be calculated"""
        self.assertEqual(roman_numerals_to_int("IX"), 9)

    def test_complex_roman_3(self):
        """Should return 5000 which needs to be calculated"""
        self.assertEqual(roman_numerals_to_int("MMMMM"), 5000)

    def test_complex_roman_4(self):
        """Should return 2999 which needs to be calculated"""
        self.assertEqual(roman_numerals_to_int("MMCMXCIX"), 2999)

    def test_complex_roman_5(self):
        """Should return 4444 which needs to be calculated"""
        self.assertEqual(roman_numerals_to_int("MMMMCDXLIV"), 4444)


if __name__ == '__main__':
    unittest.main()
