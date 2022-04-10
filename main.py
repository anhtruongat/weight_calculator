"""
Name: main.py

Description: This module displays the output of the required plates for 
the requested weight from the user
"""

from weight_calculator import WeightCalculator

def check_valid_weight(w_input: str) -> boolean:
        """ The function checks if the weight input from the user is valid.

        :param w_input: the weight input from the user
        :type w_input: str
        :return: Return True if the weight input is digit, greater than 5 
        (the minimum weight for a pair of the smallest plate, which is 2.5lb),
        and is divisible by 5, else return False
        :rtype: boolean
        """
        return w_input.isdigit() and int(w_input) >= 5 and int(w_input) % 5 == 0

def check_valid_bar(b_input: str, w_input: int) -> boolean:
    """ 
    The function checks if the weight of the bar is valid.

    :param b_input: the weight of the bar input from the user
    :type b_input: str
    :param w_input: the valid weight input 
    :type w_input: int
    :return: Return True if the weight of the bar is all digit, greater than 0, less than the weight, 
    is divisible by 5, or is blank. Otherwise, return False
    :rtype: boolean
    """
    return b_input == "" or (b_input.isdigit() and int(b_input) >= 0 and int(b_input) < w_input and int(b_input) % 5 == 0)


def display(forty_five: int, thirty_five: int, twenty_five: int, ten: int, five: int , two_half: int):
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
    weight = WeightCalculator()
    valid_weight = 0
    valid_bar_weight = 0

    print("-----------------------------------------------------------\n")
    print("                      Weight Calculator                    ")
    print("\n-----------------------------------------------------------\n")

    # Checks the weight input
    weight_input = input("Please enter a weight that is divisible by 5 and greater than the bar (lbs): ")
    while True:
        isValid = check_valid_weight(weight_input)
        if isValid:
            valid_weight = int(weight_input)
            break  
        weight_input = input("Please enter a weight that is divisible by 5 and greater than the bar (lbs): ")

    # Check the weight of the bar input
    bar_input = input("Do you want to enter a different weight for the bar (default is 45lbs)? ")
    while True:
        isValid = check_valid_bar(bar_input, valid_weight)
        if isValid:
            # If the input is blank, then set the weight of the bar to 45lbs as the default and exit the loop 
            if bar_input == "":
                valid_bar_weight = 45
            else:
                valid_bar_weight = int(bar_input)
            break

        bar_input = input("Do you want to enter a different weight for the bar (default is 45lbs)? ")


    print("\n-----------------------------------------------------------\n")
    if valid_weight == valid_bar_weight:
        print("No plates needed.")
    else:
        # If so, calculates the plates
        weight.calculate_plates(valid_weight, valid_bar_weight)

        # Display the plates
        print(f"For {valid_weight}lbs, you need: ")
        display(weight.forty_five, weight.thirty_five, weight.twenty_five, \
        weight.ten,weight.five,weight.two_half)
    print("\nThank you for using the program. Bye!\n")

if __name__ == "__main__":
    main()