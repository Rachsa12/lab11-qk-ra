# https://github.com/Rachsa12/lab11-qk-ra
# Partner 1: Quinn
# Partner 2: Rachel

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError("Cannot take the square root of a negative number")
        return math.sqrt(a)
    except TypeError:
        raise ValueError("square_root requires a numeric argument")

def hypotenuse(a, b):
    try:
        return math.hypot(a, b)  # negatives are fine
    except TypeError:
        raise ValueError("hypotenuse requires numeric arguments")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    # Per the lab spec: b / a
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def logarithm(a, b):
    # log base a of b
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid base or argument for logarithm")
    return math.log(b, a)

def exp(a, b):
    return a ** b