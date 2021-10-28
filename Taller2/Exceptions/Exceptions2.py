import math
import os
import random
import re
import sys



#
# Complete the 'FORLoop' function below.
#

def FORLoop():
    n = int(input())
    l1=[]
    for x in range(n):
        a = int(input())
        l1.append(a)
    print(l1)
    iter1 = iter(l1)
    for x in range(n):
        print(next(iter1))

    return iter1

if __name__ == '__main__':
    try:
        d = FORLoop()
        print(type(d))
        print(next(d))
  
    except StopIteration:
        print('Stop Iteration : No Next Element to fetch')