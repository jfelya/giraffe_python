from math import *

remainder = 10 % 3
# Use str() to convert any number value into a string
print("Remainder of 10 divided by 3 is: " + str(remainder))

# Testing ABS (Absolute Value)
my_num = -5
print("The absolute value of " + str(my_num) + " is: " + str(abs(my_num)))

# Testing power
pow_num1 = 3
pow_num2 = 5
print(str(pow_num1) + " to the power of " + str(pow_num2) + " is: " + str(pow(pow_num1, pow_num2)))

# max() and min() take parameters and spits out the value of the highest or lowest number in the interval
test_max = [1, 7, 9, 33]
test_min = [3259, 99, 134, 29999, 444]
print("The highest number in: " + str(test_max) + " is: " + str(max(test_max)))
print("The lowest number in: " + str(test_min) + " is: " + str(min(test_min)))

# Testing round() function
round_test = 3.59
print("Rounding: " + str(round_test) + " with the round function: " + str(round(round_test)))

# So using the import math functions allows us to use more functions regarding math, like floor and ceiling for example
floor_test = 2.9
print("Using floor() function for : " + str(floor_test) + " to: " + str(floor(floor_test)))
# same for ceil()

# Square root
sqrt_test = 36
print("Square root of " + str(sqrt_test) + " is: " + str(sqrt(sqrt_test)))
