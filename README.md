# Weight Calculator

## Overview

Weight Calculator is a Python program that calculates the amount of pre-determined barbell weights to add to a weightlifting bar to achieve a target.

The idea of this project comes from the fact that I notice that it takes me time to just figure out what kind of plate and how many plates I need for each weight that I lift. So I thought why don't I write a program to do it for me?

## Usage

Here are examples of how to use my program:

``` text

$python3 ./__main__.py
-----------------------------------------------------------

                      Weight Calculator                    

-----------------------------------------------------------

Do you want to enter a different weight for the bar (default is 45lbs)? 20
Please enter a weight that is divisible by 5 and greater than the bar weight (lbs): 55

-----------------------------------------------------------

For 55lbs, you need: 
10 plates: 2
5 plates: 2
2.5 plates: 2

Thank you for using the program. Bye!

```

``` text

$python3 ./__main__.py
-----------------------------------------------------------

                      Weight Calculator                    

-----------------------------------------------------------

Do you want to enter a different weight for the bar (default is 45lbs)? 
Please enter a weight that is divisible by 5 and greater than the bar weight (lbs): 200

-----------------------------------------------------------

For 200lbs, you need: 
45 plates: 2
25 plates: 2
5 plates: 2
2.5 plates: 2

Thank you for using the program. Bye!

```

## Tests

To run the test module:

``` text

$python3 -m unittest tests/test.py

```
