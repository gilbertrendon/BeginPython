#!/bin/python3

import sys


# Define the function 'coroutine_decorator' below
def coroutine_decorator(coroutine_func):
    def wrapper(*args, **kwdargs):
        c = coroutine_func(*args, **kwdargs)
        if c != None:
            next(c)
            return c
    return wrapper
    
# Define the coroutine function 'linear_equation' below
@coroutine_decorator
def linear_equation(a, b):
    while True:
        x = yield
        if x != None:
            e = a*(x**2)+b
            print('Expression, '+str(a)+'*x^2 + '+str(b)+', with x being '+str(x)+' equals '+str(e))
    
# Define the coroutine function 'numberParser' below
@coroutine_decorator
def numberParser():
    equation1 = linear_equation(3, 4)
    equation2 = linear_equation(2, -1)
    # code to send the input number to both the linear equations
    equation1.send(6.0)
    equation2.send(6.0)
    
def main(x):
    n = numberParser()
    if n != None:
        n.send(x)
    
if __name__ == "__main__":
    x = float(input())

    res = main(x);
    

