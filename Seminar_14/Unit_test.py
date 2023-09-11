from Task_2 import trans_data
import unittest

class TestTransDtat(unittest.TestCase):

    def test_int(self):
        self.assertEqual(trans_data("22"),22)

    def test_float(self):
        self.assertEqual(trans_data("3.14"), 3.14)

    def test_neg_float(self):
        self.assertEqual(trans_data("-3,5"), -3,5)

    def test_lowercase(self):
        self.assertEqual(trans_data("Hello World"), 'hello world')

    def test_uppercase(self):
        self.assertEqual(trans_data("ALLUPPER"), 'ALLUPPER')


if __name__ == '__main__':
    unittest.main()