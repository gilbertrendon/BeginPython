def coroutine_decorator(coroutine_func):
    def wrapper(*args, **kwdargs):
        c = coroutine_func(*args, **kwdargs)
        next(c)
        return c
    return wrapper
    
# Define the coroutine function 'linear_equation' below
@coroutine_decorator
def linear_equation(a, b):
    while True:
        x = yield
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
if __name__ == "__main__":
    a = float(input())

    b = float(input())

    equation1 = linear_equation(a, b)
    
    equation1.send(6)
    
    