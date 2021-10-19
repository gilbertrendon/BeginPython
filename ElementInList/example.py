#x:12, y:3
# def f(x):
#     return 3*x

# def g(x):
#     return 4*x

# print(f(g(2)))
def outer(x, y):

    def inner1():
        return x+y

    def inner2():
        return x*y

    return (inner1, inner2)


(f1, f2) = outer(10, 25)

print(f1())
print(f2())
