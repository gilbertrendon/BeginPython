class A:

    def __init__(self, x):
        self.__x = x

    @property
    def x(self):
        return self.__x

a = A(7)
a.x = 10
print(a.x)