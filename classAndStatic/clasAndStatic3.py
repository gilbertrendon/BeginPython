import os
import sys


        
# '''Check the Tail section for input/output'''

# if __name__ == "__main__":
#     with open(os.environ['OUTPUT_PATH'], 'w') as fout:
#         res_lst = list()
#         circcount = list()
#         lst = list(map(lambda x: float(x.strip()), input().split(',')))
#         for radi in lst:
#             c=Circle(radi)
#             res_lst.append(str(c.getCircleCount())+" : "+str(c.area()))
#         fout.write("{}".format(str(res_lst)))


#Add circle class implementation here
class Circle:
    pi = 3.14
    count = 0
    def __init__(self,radius):
        self.radius = radius
    
    @classmethod
    def getCircleCount(self):
        Circle.count += 1
        return Circle.count
  
    def area(self):
        area = self.radius **2 * Circle.pi
        return area

if __name__ == "__main__":
        #with open(os.environ['OUTPUT_PATH'], 'w') as fout:
    res_lst = list()
    circcount = list()
    lst = list(map(lambda x: float(x.strip()), input().split(',')))
    for radi in lst:
        c=Circle(radi)
        res_lst.append(str(c.getCircleCount())+" : "+str(c.area()))
    print(str(res_lst))#, str(Circle.getCircleCount()-1)