import unittest
from src.main import main

class TestStringMethods(unittest.TestCase):

    def test_1(self):
        input_file = "./gamsrv_1.in"
        output_file = "./gamsrv_1.out"
        main(input_file,output_file)
        with open(output_file, "r") as file:
            self.assertEqual('100',file.readlines()[0])

    def test_2(self):
        input_file = "./gamsrv_2.in"
        output_file = "./gamsrv_2.out"
        main(input_file,output_file)
        with open(output_file, "r") as file:
            self.assertEqual('10',file.readlines()[0])

    def test_3(self):
        input_file = "./gamsrv_3.in"
        output_file = "./gamsrv_3.out"
        main(input_file,output_file)
        with open(output_file, "r") as file:
            self.assertEqual('1000000000',file.readlines()[0])


if __name__ == '__main__':
    unittest.main()