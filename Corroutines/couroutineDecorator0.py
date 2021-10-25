#!/bin/python3

import sys
import math


# Define 'coroutine_decorator' below
def coroutine_decorator(coroutine_func):
    def wrapper(*args,**kwargs):
        c=coroutine_func(*args,**kwargs)
        next(c)
        return c
    return wrapper
    
# Define coroutine 'linear_equation' as specified in previous exercise
@coroutine_decorator
def linear_equation(a, b):
    while True:
        x=yield
        if x != None:
            e=a*(x**2)+b
            print("Expression, {0}*x^2 + {2}, with x being {1} equals {3}".format(float(a),x,float(b),float(e)))
        
        
# Define the coroutine function 'numberParser' below
@coroutine_decorator
def numberParser():
    equation1 = linear_equation(3, 4)
    equation2 = linear_equation(2, -1)
    # code to send the input number to both the linear equations
    while True :
        x = yield
        equation1.send(x)
        equation2.send(x)
        equation1 = yield
        equation2 = yield
    
if __name__ == "__main__":
    a = float(input())

    b = float(input())

    equation1 = linear_equation(a, b)
    
    next(equation1)
    
    equation1.send(6)
    
    

