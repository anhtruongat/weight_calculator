"""
This module creates the WeightCalculator class to check if the user input is valid
and calculate the quantity of plates for a specific weight that is determined by the user input.
"""

class WeightCalculator:
    """Stores the amount of each type of plate based on the user input
     for a weight and the weight of bar
    """
    DEFAULT_BAR_WEIGHT = 45

    def __init__(self):
        # The amount of a plate
        self.forty_five = 0
        # The amount of a 35lb plate
        self.thirty_five = 0
        # The amount of a 25lb plate
        self.twenty_five = 0
        # The amount of a 10lb plate
        self.ten = 0
        # The amount of a 5lb plate
        self.five = 0
        # The amount of a 2.5lb plate
        self.two_half = 0

    def check_valid_weight(self, w_input: str, b_input: int) -> bool:
        """ The method checks if the weight input from the user is valid.

        :param w_input: the weight input from the user
        :type w_input: str
        :param b_input: the valid weight of the bar
        :type b_input: int
        :return: Return True if the weight input is digit, greater than 5
        (the minimum weight for a pair of the smallest plate, which is 2.5lb),
        and is divisible by 5, else return False
        :rtype: bool
        """
        return w_input.isdigit() and int(w_input) >= 5 \
            and int(w_input) % 5 == 0 and int(w_input) > b_input

    def check_valid_bar(self, b_input: str) -> bool:
        """
        The method checks if the weight of the bar is valid.

        :param b_input: the weight of the bar input from the user
        :type b_input: str
        :return: Return True if the weight of the bar is all digit, greater than 0,
        is divisible by 5, or is blank. Otherwise, return False
        :rtype: bool
        """
        return b_input == "" or (b_input.isdigit() and int(b_input) >= 0 and int(b_input) % 5 == 0)

    def calculate_plates(self, weight: int, bar_weight: int) -> None:
        """
        The method calculates the amount of each type of plates
        on the weight and the weight of bar

        :param weight: the valid weight input
        :type weight: int
        :param bar: the valid bar weight input
        :type bar: int
        """

        # Minuses the weight of the bar from the weight
        weight -= bar_weight

        # Calculates plates from the largest to the smallest plate
        if weight >= 90:
            # Gets the quantity of the 45lb plate as a pair, so checks if the weight is
            # greater than or equal to 90 (45*2)
            self.forty_five = weight // 45
            # If the quantity is odd, decement the quantity by 1
            # because you need an even amount to put the weight in both sides of the bar
            if self.forty_five % 2 == 1:
                self.forty_five -= 1
            # Gets the remain quantity of the weight after minusing the quantity of the 45lb
            weight -= (45 * self.forty_five)

        if weight >= 70:
            # Gets the quantity of the 35lb plate as a pair, so checks if the weight is
            # greater than or equal to 70 (35*2)
            self.thirty_five = weight // 35
            # If the quantity is odd, decement the quantity by 1
            # because you need an even amount to put the weight in both sides of the bar
            if self.thirty_five % 2 == 1:
                self.thirty_five -= 1
            # Gets the remain quantity of the weight after minusing the quantity of the 35lb
            weight -= (35 * self.thirty_five)

        if weight >= 50:
            # Gets the quantity of the 25lb plate as a pair, so checks if the weight is
            # greater than or equal to 50 (25*2)
            self.twenty_five = weight // 25
            # If the quantity is odd, decement the quantity by 1
            # because you need an even amount to put the weight in both sides of the bar
            if self.twenty_five % 2 == 1:
                self.twenty_five -= 1
            # Gets the remain quantity of the weight after minusing the quantity of the 25lb
            weight -= (25 * self.twenty_five)

        if weight >= 20:
            # Gets the quantity of the 10lb plate as a pair, so checks if the weight is
            # greater than or equal to 20 (10*2)
            self.ten = weight // 10
            # If the quantity is odd, decement the quantity by 1
            # because you need an even amount to put the weight in both sides of the bar
            if self.ten % 2 == 1:
                self.ten -= 1
            # Gets the remain quantity of the weight after minusing the quantity of the 10lb
            weight -= (10 * self.ten)

        if weight >= 10:
            # Gets the quantity of the 5lb plate as a pair, so checks if the weight is
            # greater than or equal to 10 (5*2)
            self.five = weight // 5
            # If the quantity is odd, decement the quantity by 1
            # because you need an even amount to put the weight in both sides of the bar
            if self.five % 2 == 1:
                self.five -= 1
            # Gets the remain quantity of the weight after minusing the quantity of the 5lb
            weight -= (5 * self.five)

        if weight >= 5:
            # Gets the quantity of the 2.5lb plate as a pair, so checks if the weight is
            # greater than or equal to 5 (2.5*2)
            self.two_half = int(weight // 2.5)
            # If the quantity is odd, decement the quantity by 1
            # because you need an even amount to put the weight in both sides of the bar
            if self.two_half % 2 == 1:
                self.two_half -= 1
            # Gets the remain quantity of the weight after minusing the quantity of the 2.5lb
            weight -= (2.5 * self.two_half)
