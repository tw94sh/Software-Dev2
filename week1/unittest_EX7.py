import EX7
import unittest
from unittest.mock import patch, mock_open

class EqnSolveInputTest(unittest.TestCase):
    
    #fake data in file
    txt_file = """16 200 -10
    12
    70
    1
    999
    50
    20
    1000
    150
    300
    200
    90
    900
    40
    140
    130
    30"""

    #check file input

    #correct format and input
    def test_txt_file_input(self):
        with patch('builtins.open', mock_open(read_data= self.txt_file)) as f:
            check = EX7.EqnSolve('/dev/null') #fake file path
            self.assertEqual(check, [50, 150, 20, 70, 90, 40, 130, 30])
    
    #input not string
    def test_invalid_txt_file_input(self):
        with patch('builtins.open', mock_open(read_data= self.txt_file)) as f:
            check = EX7.EqnSolve([1])
            self.assertEqual(check, 'Invalid file name')

    #input is None
    def test_None_txt_file_input(self):
        with patch('builtins.open', mock_open(read_data= self.txt_file)) as f:
            check = EX7.EqnSolve(None)
            self.assertEqual(check, 'Invalid file name')

#run this code if and only if it's the main file
if __name__ == '__main__':
    unittest.main()