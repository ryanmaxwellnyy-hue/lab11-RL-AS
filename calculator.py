# https://github.com/newmanhw/lab11-RL-AS
# Partner 1: Ryan Leitner
# Partner 2: Aung Sett

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

def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b
def div(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
    except ZeroDivisionError as e:
        raise e
def logarithm(a, b):
    if a <= 0 or b <= 0 or a == 1:
        raise ValueError("Invalid inputs: base and value must be positive, base cannot be 1.")
    return math.log(b, a)

def exp(a, b):
    return a ** b