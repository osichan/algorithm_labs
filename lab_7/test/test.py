import unittest
from src.main import main


class TestStringMethods(unittest.TestCase):
    def test_1(self):
        input_file = "ijones_1.in"
        output_file = "ijones_1.out"
        main(input_file, output_file)
        with open(output_file, "r") as file:
            self.assertEqual("5", file.readlines()[0])

    def test_2(self):
        input_file = "ijones_2.in"
        output_file = "ijones_2.out"
        main(input_file, output_file)
        with open(output_file, "r") as file:
            self.assertEqual("2", file.readlines()[0])

    def test_3(self):
        input_file = "ijones_3.in"
        output_file = "ijones_3.out"
        main(input_file, output_file)
        with open(output_file, "r") as file:
            self.assertEqual("201684", file.readlines()[0])


if __name__ == "__main__":
    unittest.main()
