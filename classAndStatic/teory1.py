# class Circle(object):
#     def __init__(self, radius):
#         self.__radius = radius
#     @staticmethod
#     def square(x):
#         return x**2
#     def area(self):
#         return 3.14*self.square(self.__radius)
# c1 = Circle(3.9)
# print(c1.area())  

# class A:

#     @staticmethod
#     def m1(self):
#         print('Static Method')

#     @classmethod
#     def m1(self):
#         print('Class Method')

# A.m1()

#What is the output of the following code?

# class A:

#     @classmethod
#     def m1(self):
#         print('In Class A, Class Method m1.')

#     def m1(self):
#         print('In Class A, Method m1.')

# a = A()

# a.m1()

# def s1(x, y):
#     return x*y

# class A:

#     @staticmethod
#     def s1(x, y):
#         return x + y

#     def s2(self, x, y):
#         return s1(x, y)

# a = A()
# print(a.s2(3, 7))

class A:

    @classmethod
    def getC(self):
        print('In Class A, method getC.')

class B(A):
    pass

b = B()
B.getC()
b.getC()