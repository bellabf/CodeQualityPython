"""
This module contains basic mathematical functions such as addition, division,
factorial calculation, and result printing.
"""

def add(a, b):
    """Returns the sum of two numbers."""
    result = a + b
    return result

def divide_numbers(a, b):
    """Returns the result of dividing `a` by `b`, or prints an error if `b` is 0."""
    if b != 0:
        return a / b
    print("Error: division by zero!")
    return None

def factorial(n):
    """Returns the factorial of a number `n`."""
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f

def print_result(x):
    """Prints the result if it is not None."""
    if x is not None:
        print("The result is: " + str(x))

VAL1 = 10
VAL2 = 0
SUM = add(VAL1, VAL2)
division = divide_numbers(10, 0)
fact = factorial(5)
print_result(sum)
print_result(fact)
