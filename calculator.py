# https://github.com/Irkling/lab10-EL-ZL
# Partner 1: Erik Liddle
# Partner 2: Zhiheng Liu
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math

def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)

def hypotenuse(a, b):

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def log(a, b):
    return math.log(a, b)

def power(a, b):
    return a ** b



