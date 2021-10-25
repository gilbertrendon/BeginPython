
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

if __name__ == '__main__':
    print('')
    n = int(input().strip())
    
    for i in generator_Magic(n):
        print(int(i))

    gen1 = generator_Magic(n)
    print(type(gen1))
