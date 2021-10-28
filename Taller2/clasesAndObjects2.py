import math
import os
import random
import re
import sys

# Write your code here
class RectangleSquare():
    def __init__(self, l, w, s):
        self.length = l
        self.width  = w
        self.s  = s

        
    def display_rectangle(self):
        print('This is a Rectangle')

    def rectangle_area(self):
        print('Area of Rectangle is ',self.length*self.width)
        return self.length*self.width
    
    def display_square(self):
        print('This is a Square')
    
    def square_area(self):
        print('Area of square is ',self.s*self.s)

if __name__ == '__main__':
    
    l = int(input())
    b = int(input())
    s = int(input())

    obj1 = RectangleSquare(l,b,s)
    obj1.display_rectangle()
    obj1.rectangle_area()
    obj1.display_square()
    obj1.square_area()
   
