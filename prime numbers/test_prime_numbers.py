import unittest
from prime_numbers import prime_numbers


class MyTestCase(unittest.TestCase):

    def test_not_int(self):
        """Should return [] if not int was passed"""
        self.assertEqual(prime_numbers(2.4, 120), [])

    def test_low_greater_than_high(self):
        """Should return [] if low is greater than high"""
        self.assertEqual(prime_numbers(10, 3), [])

    def test_low_negative(self):
        """Should return [] if low is negative"""
        self.assertEqual(prime_numbers(-1, 10), [])

    def test_no_prime_nums(self):
        """Should return [] if there's no prime nums in given interval"""
        self.assertEqual(prime_numbers(20, 22), [])

    def test_zero_to_one_interval(self):
        """Should return [] if interval is [0, 1]"""
        self.assertEqual(prime_numbers(0, 1), [])

    def test_prime_numbers_1(self):
        """Should return [2, 3, 5, 7] """
        self.assertEqual(prime_numbers(1, 10), [2, 3, 5, 7])

    def test_prime_numbers_2(self):
        """Should return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                          53, 59, 61, 67, 71, 73, 79, 83, 89, 97]"""
        self.assertEqual(prime_numbers(1, 100), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                                                 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

    def test_prime_numbers_3(self):
        """Should return [2]"""
        self.assertEqual(prime_numbers(0, 2), [2])

    def test_prime_numbers_4(self):
        """Should return [14, 17]"""
        self.assertEqual(prime_numbers(14, 17), [17])

    def test_prime_numbers_5(self):
        """Should return [2, 3, 5, 7, 11, 13]"""
        self.assertEqual(prime_numbers(0, 16), [2, 3, 5, 7, 11, 13])


if __name__ == '__main__':
    unittest.main()
