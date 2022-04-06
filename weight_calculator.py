from re import T
from typing import List, Dict
from collections import defaultdict
import sys

class Weight:
    def __init__(self):
        self.forty_five = 0
        self.thirty_five = 0
        self.twenty_five = 0
        self.ten = 0
        self.five = 0
        self.two_half = 0

    def check_valid_input(self):
        weight = ""
        bar = ""

        while True:
            weight = input("Please enter a weight that is divisible by 5 and greater than the bar (lbs): ")
            if weight.isdigit() and int(weight) >= 5 and int(weight) % 5 == 0:
                weight = int(weight)
                break

        while True:
            barInput = input("Do you want to enter a different weight for the bar (default is 45lbs)? (y/n) ")
            if barInput == "y":
                bar = input("Please enter the weight of the bar: ")
                if bar.isdigit() and int(bar) > 0 and int(bar) < weight and int(bar) % 5 == 0: 
                    bar = int(bar)
                    break
            else:
                bar = 45
                break 

        return weight, bar

    def calculate_plates(self, weight, bar):
        forty_five_pounds = 45
        thirty_five_pounds = 35
        twenty_five_pounds = 25
        ten_pounds = 10
        five_pounds = 5
        two_half_pounds = 2.5 

        #minus the weight of the bar
        weight -= bar

        #calculate plates from the largest to the smallest plate
        if weight >= 90:
            self.forty_five = weight // forty_five_pounds
            if self.forty_five % 2 == 1:
                self.forty_five -= 1
            weight -= (forty_five_pounds * self.forty_five)

        if weight >= 70:
            self.thirty_five = weight // thirty_five_pounds
            if self.thirty_five % 2 == 1:
                self.thirty_five -= 1
            weight -= (thirty_five_pounds * self.thirty_five) 

        if weight >= 50:
            self.twenty_five = weight // twenty_five_pounds
            if self.twenty_five % 2 == 1:
                self.twenty_five -= 1
            weight -= (twenty_five_pounds * self.twenty_five)

        if weight >= 20:
            self.ten = weight // ten_pounds
            if self.ten % 2 == 1:
                self.ten -= 1
            weight -= (ten_pounds * self.ten)

        if weight >= 10:
            self.five = weight // five_pounds
            if self.five % 2 == 1:
                self.five -= 1
            weight -= (five_pounds * self.five)

        else:
            self.two_half = weight // two_half_pounds
            if self.two_half % 2 == 1:
                self.two_half -= 1
            weight -= (two_half_pounds * self.two_half)

def display(forty_five,thirty_five,twenty_five,ten,five,two_half):
    if forty_five != 0:
        print(f"45 plate(s): {forty_five}")
    if thirty_five != 0:
        print(f"35 plate(s): {thirty_five}")
    if twenty_five != 0:
        print(f"25 plate(s): {twenty_five}")
    if ten != 0:
        print(f"10 plate(s): {ten}")
    if five != 0:
        print(f"5 plate(s): {five}")
    if two_half != 0:
        print(f"2.5 plate(s): {two_half}")

if __name__ == "__main__":
    weight = Weight()

    print("----Weight Calculator----")
    
    # check the user input if it is valid
    valid_weight, valid_bar_weight = weight.check_valid_input()
        
    # if so, calculate the plates
    weight.calculate_plates(valid_weight, valid_bar_weight)

    # display the plates
    print(f"For {valid_weight}lbs, you need: ")
    display(weight.forty_five, weight.thirty_five, weight.twenty_five, \
    weight.ten,weight.five,weight.two_half)


