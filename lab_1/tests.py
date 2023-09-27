import unittest
from main import zigzag_array

class TestStringMethods(unittest.TestCase):

    def test_1(self):
        self.assertEqual(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
            ,
                         zigzag_array([
                             [1, 2, 6, 7, 15],
                             [3, 5, 8, 14, 16],
                             [4, 9, 13, 17, 22],
                             [10, 12, 18, 21, 23],
                             [11, 19, 20, 24, 25]
                         ]))

    def test_2(self):
        self.assertEqual(
            [1, 2, 3, 4, 5, 6, 7, 8]
            ,
            zigzag_array([
                [1, 2, 5, 6],
                [3, 4, 7, 8]
            ]))

    def test_3(self):
        self.assertEqual(
            [1, 2, 3, 4, 5, 6]
            ,
            zigzag_array([
                [1, 2, 3, 4, 5, 6]
            ]))

    def test_4(self):
        self.assertEqual([
            1
        ],
            zigzag_array([
                [1]
            ]))

if __name__ == '__main__':
    unittest.main()