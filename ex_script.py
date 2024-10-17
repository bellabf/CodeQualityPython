"""
This module provides addition, division, and factorial functions.
"""


def add(a, b):
    """
    Add two numbers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of a and b.
    """
    result = a + b
    return result


def divide_numbers(a, b):
    """
    Divide two numbers.

    Args:
        a (int or float): The numerator.
        b (int or float): The denominator.

    Returns:
        float or None: The result of a/b, or None if division by zero occurs.
    """
    if b != 0:
        return a / b

    print("Error: division by zero!")
    return None


def factorial(n):
    """
    Calculate the factorial of a number.

    Args:
        n (int): The number to calculate the factorial of.

    Returns:
        int: The factorial of n.
    """
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f


def print_result(x):
    """
    Print the result if it's not None.

    Args:
        x (int or float or None): The value to print.
    """
    if x is not None:
        print("The result is: " + str(x))


VAL1 = 10
VAL2 = 0
RESULT_SUM = add(VAL1, VAL2)
DIVISION = divide_numbers(10, 0)
FACT = factorial(5)

print_result(RESULT_SUM)
print_result(FACT)
