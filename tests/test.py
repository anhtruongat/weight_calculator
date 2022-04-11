"""
This module does unittest for the weight calculator script.
"""

import unittest
from weight_calculator import WeightCalculator  # pylint:disable=import-error

class TestWeightCalculator(unittest.TestCase):
    """This class tests the check_valid_weight,
    check_valid_bar, and calculate_plates method's functionality"""
    def setUp(self) -> None:
        self.weight = WeightCalculator()

    def test_check_valid_weight(self) -> None:
        """
        This method tests invalid input for weights.
        """
        result = self.weight.check_valid_weight("", 45)
        self.assertFalse(result)
        result = self.weight.check_valid_weight("-1", 45)
        self.assertFalse(result)
        result = self.weight.check_valid_weight("4", 45)
        self.assertFalse(result)
        result = self.weight.check_valid_weight("abc", 45)
        self.assertFalse(result)
        result = self.weight.check_valid_weight("~", 45)
        self.assertFalse(result)
        result = self.weight.check_valid_weight("35", 45)
        self.assertFalse(result)

    def test_check_valid_bar(self) -> None:
        """
        This method tests invalid input for the weight of the bar
        """
        result = self.weight.check_valid_bar("-1")
        self.assertFalse(result)
        result = self.weight.check_valid_bar("abc")
        self.assertFalse(result)
        result = self.weight.check_valid_bar("~")
        self.assertFalse(result)
        result = self.weight.check_valid_bar("8")
        self.assertFalse(result)
        result = self.weight.check_valid_bar("101")
        self.assertFalse(result)

    def test_calculate_plates(self) -> None:
        """
        This method tests calculate_plates method 
        for 55lbs of the weight and 20 lbs of the bar weight
        """
        self.weight.calculate_plates(55, 20)
        self.assertEqual(self.weight.forty_five, 0)
        self.assertEqual(self.weight.thirty_five, 0)
        self.assertEqual(self.weight.twenty_five, 0)
        self.assertEqual(self.weight.ten, 2)
        self.assertEqual(self.weight.five, 2)
        self.assertEqual(self.weight.two_half, 2)

    def test_calculate_plates_2(self) -> None:
        """
        This method tests calculate_plates method 
        for 155lbs of the weight and 45 lbs of the bar weight
        """
        self.weight.calculate_plates(155, 45)
        self.assertEqual(self.weight.forty_five, 2)
        self.assertEqual(self.weight.thirty_five, 0)
        self.assertEqual(self.weight.twenty_five, 0)
        self.assertEqual(self.weight.ten, 2)
        self.assertEqual(self.weight.five, 0)
        self.assertEqual(self.weight.two_half, 0)

    def test_calculate_plates_3(self) -> None:
        """
        This method tests calculate_plates method 
        for 200lbs of the weight and 45 lbs of the bar weight
        """
        self.weight.calculate_plates(200, 45)
        self.assertEqual(self.weight.forty_five, 2)
        self.assertEqual(self.weight.thirty_five, 0)
        self.assertEqual(self.weight.twenty_five, 2)
        self.assertEqual(self.weight.ten, 0)
        self.assertEqual(self.weight.five, 2)
        self.assertEqual(self.weight.two_half, 2)

if __name__ == "__main__":
    unittest.main()
