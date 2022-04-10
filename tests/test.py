"""
Name: tests.py

Description: This module does unittest for the weight calculator script.
"""

import unittest
from main import check_valid_weight,check_valid_bar

class TestWeightCalculator(unittest.TestCase):
    def test_check_valid_weight(self) -> None:
        """
        This method tests invalid input for weights 
        """
        result = check_valid_weight("")
        self.assertFalse(result)
        result = check_valid_weight("-1")
        self.assertFalse(result)
        result = check_valid_weight("4")
        self.assertFalse(result)
        result = check_valid_weight("abc")
        self.assertFalse(result)
        result = check_valid_weight("~")
        self.assertFalse(result)

    def test_check_valid_bar(self) -> None:
        """
        This method tests invalid input for the weight of the bar
        """
        result = check_valid_bar("-1", 55)
        self.assertFalse(result)
        result = check_valid_bar("abc", 55)
        self.assertFalse(result)
        result = check_valid_bar("~", 55)
        self.assertFalse(result)
        result = check_valid_bar("8", 55)
        self.assertFalse(result)
        result = check_valid_bar("60", 55)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
