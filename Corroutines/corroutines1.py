# def TokenIssuer():
#     tokenId = 0
#     while True:
#         name = yield
#         tokenId += 1
#         print('Token number of', name, ':', tokenId)
# t = TokenIssuer()
# next(t)
# t.send('George')
# t.send('Rosy')
# t.send('Smith')

# def TokenIssuer(tokenId=0):
#     try:
#        while True:
#             name = yield
#             tokenId += 1
#             print('Token number of', name, ':', tokenId)
#     except GeneratorExit:
#         print('Last issued Token is :', tokenId)
# t = TokenIssuer(100)
# next(t)
# t.send('George')
# t.send('Rosy')
# t.send('Smith')
# t.close()
#******************************************************************************
# def coroutine_decorator(func):
#     def wrapper(*args, **kwdargs):
#         c = func(*args, **kwdargs)
#         next(c)
#         return c
#     return wrapper
# @coroutine_decorator
# def TokenIssuer(tokenId=0):
#     try:
#         while True:
#             name = yield
#             tokenId += 1
#             print('Token number of', name, ':', tokenId)
#     except GeneratorExit:
#         print('Last issued Token is :', tokenId)
# t = TokenIssuer(100)
# t.send('George')
# t.send('Rosy')
# t.send('Smith')
# t.close()
# def nameFeeder():
#     while True:
#         fname = yield
#         print('First Name:', fname)
#         lname = yield
#         print('Last Name:', lname)

# n = nameFeeder()
# next(n)
# n.send('George')
# n.send('Williams')
# n.send('John')
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
# def outer(x, y):

#     def inner1():
#         return x+y

#     def inner2():
#         return x*y

#     return (inner1, inner2)


# (f1, f2) = outer(10, 25)

# print(f1())
# print(f2())
# def bind(func):
#     func.data = 9
#     return func

# @bind
# def add(x, y):
#     return x + y

# print(add(3, 10))
# print(add.data)
from contextlib import contextmanager

@contextmanager
def context():
    print('Entering Context')
    yield 
    print("Exiting Context")

with context():
    print('In Context')