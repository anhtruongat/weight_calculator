from weight_calculator import WeightCalculator

def display(forty_five: int, thirty_five: int, twenty_five: int, ten: int, five: int , two_half: int):
    """
    Parameters: - the quantity of 45lb plate
                - the quantity of 35lb plate
                - the quantity of 25lb plate
                - the quantity of 10lb plate
                - the quantity of 5lb plate
                - the quantity of 2.5lb plate
    
    Return: None
    
    Description: This function displays the quantity of each plate (if the quantity is not zero)
    that the user needs for both sides of the bar
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
    
    print("-----------------------------------------------------------\n")
    print("                      Weight Calculator                    ")
    print("\n-----------------------------------------------------------\n")

    # Checks the user input if they are valid
    valid_weight, valid_bar_weight = weight.check_valid_input()
        
    # If so, calculates the plates
    weight.calculate_plates(valid_weight, valid_bar_weight)

    # Display the plates
    print("\n-----------------------------------------------------------\n")
    print(f"For {valid_weight}lbs, you need: ")
    display(weight.forty_five, weight.thirty_five, weight.twenty_five, \
    weight.ten,weight.five,weight.two_half)
    print("\nThank you for using the program. Bye!\n")

if __name__ == "__main__":
    main()