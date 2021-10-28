import math
import os
import random
import re
import sys



#
# Complete the 'primegenerator' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER num
#  2. INTEGER val
#

#def primegenerator(num, val):
    # Write your code here
def primenum(num, val):
    primes = []
    for i in range(2, num):
        for j in range(2, int(i / 2) + 1):
            if i % j == 0:
                break
        else:
            primes.append(i)
        
    for i in range(1 - val, len(primes), 2):
        yield primes[i]

prime1 = list(primenum(21, 0)) # [3, 7, 13, 19]
prime2 = list(primenum(21, 1)) # [2, 5, 11, 17]


if __name__ == '__main__':

    num = int(input().strip())

    val = int(input().strip())

    for i in primenum(num, val):
        print(i,end=" ")