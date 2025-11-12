"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def log(a, b):
    if a <= 0 or b <= 0 or b == 1:
        raise ValueError("Logarithm domain error: a and b must be positive, and b cannot be 1.")
    return math.log(a, b)

def exp(a, b):
    return a ** b