# Weight Calculator

## Overview

Weight Calculator is a Python program that calculates the amount of pre-determined barbell weights to add to a weightlifting bar to achieve a target.

The idea of this project comes from the fact that I notice that it takes me time to just figure out what kind of plate and how many plates I need for each weight that I lift. Therefore, I think why don't I write a program to do it for me. Hence, this project was born.

## Usage
Here are examples of how to use my program:
```
$python3 ./main.py
---------------------------------------------

             Weight Calculator                    

---------------------------------------------

Please enter a weight that is divisible by 5 and greater than the bar (lbs): 200
Do you want to enter a different weight for the bar (default is 45lbs)? 

---------------------------------------------

For 200lbs, you need: 
45 plates: 2
25 plates: 2
5 plates: 2
2.5 plates: 2

Thank you for using the program. Bye!
```

```
$python3 ./main.py
---------------------------------------------

             Weight Calculator                    

---------------------------------------------

Please enter a weight that is divisible by 5 and greater than the bar (lbs): 55
Do you want to enter a different weight for the bar (default is 45lbs)? 20

---------------------------------------------

For 55lbs, you need: 
10 plates: 2
5 plates: 2
2.5 plates: 2

Thank you for using the program. Bye!
```