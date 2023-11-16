# test_PPTmaker.py

import unittest
from PPTmaker import gpt_pptmaker

class TestPPTMaker(unittest.TestCase):
    def test_create_ppt(self):
        # Test case 1: Check if the function returns a string
        result = gpt_pptmaker("nothing", "",\
                               "")
        self.assertIsInstance(result[0], str)
        
        # Test case 2: Check if the function returns the correct output
        expected_output = "Slide"
        self.assertEqual(result[0][:5], expected_output)
        
        # Test case 3: Check if the function raises an error when given invalid input
        with self.assertRaises(TypeError):
            gpt_pptmaker(123, ["test_body"])