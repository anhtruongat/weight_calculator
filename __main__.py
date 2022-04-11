"""
This module displays the output of the required plates for the requested weight from the user
"""

from weight_calculator import WeightCalculator  # pylint:disable=import-error

def display(forty_five: int, thirty_five: int, twenty_five: int, \
    ten: int, five: int , two_half: int):
    """
    This function displays the quantity of each plate (if the quantity is not zero)
    that the user needs for both sides of the bar.
    :param forty_five: the quantity of 45lb plate
    :type forty_five: int
    :param thirty_five: the quantity of 35lb plate
    :type thirty_five: int
    :param twenty_five: the quantity of 25lb plate
    :type twenty_five: int
    :param ten: the quantity of 10lb plate
    :type ten: int
    :param five: the quantity of 5lb plate
    :type five: int
    :param two_half: the quantity of 2.5lb plate
    :type two_half: int
    """

    # Checks the quantity of each plate, if the quantity is not zero, displays the amount
    if forty_five != 0:
        print(f"45 plates: {forty_five}")
    if thirty_five != 0:
        print(f"35 plates: {thirty_five}")
    if twenty_five != 0:
        print(f"25 plates: {twenty_five}")
    if ten != 0:
        print(f"10 plates: {ten}")
    if five != 0:
        print(f"5 plates: {five}")
    if two_half != 0:
        print(f"2.5 plates: {two_half}")

def main():
    """This function asks for user input and displays
    the quantity of plates based on that input"""
    calculator = WeightCalculator()
    valid_weight = 0
    valid_bar_weight = 0

    print("-----------------------------------------------------------\n")
    print("                      Weight Calculator                    ")
    print("\n-----------------------------------------------------------\n")

    # Check the weight of the bar input
    while True:
        bar_input = input(
            "Do you want to enter a different weight "
            "for the bar (default is 45lbs)? "
        )
        is_valid = calculator.check_valid_bar(bar_input)
        if is_valid:
            # If the input is blank, then set the weight
            # of the bar to 45lbs as the default and exit the loop
            if bar_input == "":
                valid_bar_weight = calculator.DEFAULT_BAR_WEIGHT
            else:
                valid_bar_weight = int(bar_input)
            break

    # Checks the weight input
    while True:
        weight_input = input(
            "Please enter a weight that is divisible by 5 "
            "and greater than the bar weight (lbs): "
        )
        is_valid = calculator.check_valid_weight(weight_input, valid_bar_weight)
        if is_valid:
            valid_weight = int(weight_input)
            break

    # If so, calculates the plates
    calculator.calculate_plates(valid_weight, valid_bar_weight)
    print("\n-----------------------------------------------------------\n")
    # Display the plates
    print(f"For {valid_weight}lbs, you need: ")
    display(calculator.forty_five, calculator.thirty_five, calculator.twenty_five, \
    calculator.ten, calculator.five, calculator.two_half)
    print("\nThank you for using the program. Bye!\n")

if __name__ == "__main__":
    main()
