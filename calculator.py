#https://github.com/CLeander321/lab10--CL---MM-.git
#Person1 Chloe leander
#persone2 Maliha Mokamlel
import math
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
def square_root(a):
    if a < 0:
        raise ValueError
    return math.sqrt(a)
def hypotenuse(a, b):
    return math. hypot(a, b)
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def mul(a, b):
    return a * b
def divide(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a
def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a
def logarithm(a, b):
    if a<=0 or a==1:
        raise ValueError
    if b<=0:
        raise ValueError
    return math.log(a, b)
def log(a, b):
    if a<=0 or a==1:
        raise ValueError
    if b <= 0:
        raise ValueError
    return math.log(a, b)
def exponent(a, b):
    return a ** b
def exp(a, b):
    return a ** b

