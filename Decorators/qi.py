# # def smart_divide(func):
# #     def wrapper(*args):
# #         a, b = args
# #         if b == 0:
# #             print('oops! cannot divide')
# #             return
# #         return func(*args)
# #     return wrapper


# # @smart_divide
# # def divide(a, b):
# #     return a / b

# # print(divide.__name__)
# # print(divide(4, 16))
# # print(divide(8,0))

# # def bind(func):
# #     func.data = 9
# #     return func

# # @bind
# # def add(x, y):
# #     return x + y

# # print(add(3, 10))
# # print(add.data)
# def decorator_func(func):
#     def wrapper(*args, **kwdargs):
#         return func(*args, **kwdargs)
#     wrapper.__name__ = func.__name__
#     return wrapper


# @decorator_func
# def square(x):
#     return x**2

# print(square.__name__)
# from functools import wraps

# def decorator_func(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         return func(*args, **kwargs)
#     return wrapper

# @decorator_func
# def square(x):
#     return x**2
# print(square.__name__)
#1. define a decorator function log which logs information on a function and thearguments passed to it
def log(func):

    def inner(*args, **kwdargs):

        STDOUT= "Accessed the function -'{}' with arguments {}{}".
        format(func.__name__, args, kwdargs) 
        return STDOUT 
    return inner
    def greet(msg): 'Greeting Message : ' + msg greet = log(greet)

if __name__ == "__main__":
    with open(os.environ['OUTPUT_PATH'], 'w') as fout:
        res_lst = list()
        res_lst.append(greet(str(input())))
        fout.write("{}".format(*res_lst))