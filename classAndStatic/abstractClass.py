# class Circle():
#     def __init__(self, radius):
#         self.__radius = radius
#     @staticmethod
#     def square(x):
#         return x**2
#     def area(self):
#         return 3.14*self.square(self.__radius)
#     def perimeter(self):
#         return 2*3.14*self.__radius
# c1 = Circle(3.9)
# print(c1.area())
# from abc import ABC, abstractmethod

# class A(ABC):
    
#     @abstractmethod
#     def m1():
#         print('In class A, Method m1.')

#     def m2():
#         print('In class A, Method m2.') 

# class B(A):

#     def m2():
#         print('In class B, Method m2.')

# b = B()
# b.m2()
from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def m1():
        print('In class A.')

a = A()
a.m1()
