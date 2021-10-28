import os
import sys
import math
class Circle:
    def __init__(self, radius):
        self.pi = 3.14
        self.radius = radius

    def area(self):
        return self.pi * self.radius**2

    def circumference(self):
        return 2*self.pi * self.radius
if __name__ == "__main__":
    #with open(os.environ['OUTPUT_PATH'], 'w') as fout:
    res_lst = list()
    lst = list(map(lambda x: float(x.strip()), input().split(',')))
    for radius in lst:
        res_lst.append(round(Circle(radius).area(),2))
    print(str(res_lst))
    print(len(lst))
        #fout.write("{}\n{}".format(str(res_lst), str(Circle.no_of_circles)))
