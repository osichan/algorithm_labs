import unittest
from src.main import transitions_init


class TestStringMethods(unittest.TestCase):
    def test_1(self):
        haystack = "ababcdeabcabcabc"

        needle = "abc"
        result = transitions_init(haystack, needle)
        self.assertEqual([2, 7, 10, 13], result)

    def test_2(self):
        # Test case with an empty haystack
        haystack = ""
        needle = "abc"
        result = transitions_init(haystack, needle)
        self.assertEqual([], result)

    def test_3(self):
        # Test case with an empty needle
        haystack = "abababababababab"
        needle = ""
        result = transitions_init(haystack, needle)
        self.assertEqual([], result)

    def test_4(self):
        # Test case with needle not present in haystack
        haystack = "abababababababab"
        needle = "xyz"
        result = transitions_init(haystack, needle)
        self.assertEqual([], result)


if __name__ == "__main__":
    unittest.main()
