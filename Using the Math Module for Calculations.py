# Task 2: Using the Math Module for Calculations

import math

# Ask user for a number
number = float(input("Enter a number: "))

# Calculate square root, natural logarithm, and sine
sqrt_value = math.sqrt(number)
log_value = math.log(number)  # natural log (log base e)
sine_value = math.sin(number)  # sine of the number in radians

# Display the calculated results
print(f"The square root of {number} is {sqrt_value}")
print(f"The natural logarithm (log base e) of {number} is {log_value}")
print(f"The sine of {number} (in radians) is {sine_value}")
