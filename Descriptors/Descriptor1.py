
import sys
import os



class Celsius:
    def __init__(self, temp = 0):
        self.temp = temp
    def to_fahrenheit(self):
        return (self.temp * 1.8) + 32
    def __get__(self):
        return(self.temp)
    def __set__(self,temp):
        self.temp=temp
    desc=property(__get__,__set__)
class Temperature:
   def __init__(self,temp=0):
       self.fahrenheit=temp
       self.celsius=(((self.fahrenheit-32)*5)/9)
       c=Celsius()
       c.desc=self.celsius
       self.fahrenheit=c.to_fahrenheit()
        
'''Check the Tail section for input/output'''

if __name__ == "__main__":
    with open(os.environ['OUTPUT_PATH'], 'w') as fout:
        res_lst = list()
        t1 = Temperature(int(input()))
        res_lst.append((int(t1.fahrenheit), t1.celsius))
        t1.celsius = int(input())
        res_lst.append((t1.fahrenheit, float(t1.celsius)))
        fout.write("{}\n{}".format(*res_lst))