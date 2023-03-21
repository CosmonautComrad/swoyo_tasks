import unittest
from text_stat import text_stat


class MyTestCase(unittest.TestCase):
    def test_incorrect_file(self):
        """Should return dictionary with error 'No such file or directory'"""
        self.assertEqual(text_stat("./data/missing.txt"), {"error": "No such file or directory"})

    def test_empty_file(self):
        """Should work correctly with empty files"""
        self.assertEqual(text_stat("./data/empty.txt"), {'word_amount': 0, 'paragraph_amount': 0,
                                                         'bilingual_word_amount': 0})


if __name__ == '__main__':
    unittest.main()
