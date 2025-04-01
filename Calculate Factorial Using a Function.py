# Task 1: Calculate Factorial Using a Function

# Function to calculate factorial using a loop
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example: Call the function with the number 5
number = 5
fact = factorial(number)
print(f"The factorial of {number} is {fact}")
