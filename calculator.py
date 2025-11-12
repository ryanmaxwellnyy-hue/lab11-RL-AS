

import math


def square_root(a):
    try:
        if a < 0:
            raise ValueError("Cannot take the square root of a negative number.")
        return math.sqrt(a)
    except ValueError as e:
        raise e

def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except Exception as e:
        raise e
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def log(a, b):
    if a <= 0 or b <= 0 or b == 1:
        raise ValueError("Logarithm domain error: a and b must be positive, and b cannot be 1.")
    return math.log(a, b)

def exp(a, b):
    return a ** b