"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example

import math

def square_root(a):
    if a <0:
        raise ValueError
    return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)


def add(a, b): 
    c= a + b
    return c

def subtract(a, b):
    c = a-b
    return c

def multiply(a,b):
    c = a *b
    return c

def divide(a, b):
    if a ==0:
        raise ZeroDivisionError
    c = b/a
    return c

def logarithm(a, b):
    if b <=0:
        raise ValueError
    c=math.log(b, a)
    return c

def exponent(a,b):
    c=a**b
    return c





