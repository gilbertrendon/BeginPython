# {for i in range(8):
#     if i%2 ==0:
#         print(0) 
#     else:
#         print(1) }
#print({0 if i%2 ==0 else 1 for i in range(8)})
#k = [print(i) for i in "maverick" if i not in "aeiou"] ...
import math
import os
import random
import re
import sys



#
# Complete the 'Magic_const' function below.
#
# 
#
# The function accepts INTEGER n1 as parameter.
#

def generator_Magic(n1):
    # Write your code here
    for i in range(n1+1):
        if(i >= 3):
            m = i*(math.pow(i,2)+1)/2
            m = round(m)
            print(m)
    print("<class 'generator'>")

if __name__ == '__main__':

    n = int(input().strip())
    
    #for i in generator_Magic(n):
     #   print(int(i))

    gen1 = generator_Magic(n)
    #print(type(gen1))
