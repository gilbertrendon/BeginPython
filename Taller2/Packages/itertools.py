
import math
import os
import random
import re
import sys
import itertools
import operator
def performIterator(tuplevalues):

    l1=[]
    l2=[]
    for x in range(4):
        l2.append(tuplevalues[0][x])

    t2=tuple(l2)
    l1.append(t2)

    ll=[tuplevalues[1][0] for x in range(len(tuplevalues[1]))]

    t3=tuple(ll)
    l1.append(t3)

    t4=tuple(itertools.accumulate(tuplevalues[2]))
    l1.append(t4)

    f=[]
    for x in tuplevalues:
        for y in x:
            f.append(y)
    l1.append(tuple(f))

    ff = itertools.filterfalse(lambda x: x%2==0,f)
    l1.append(tuple(ff))

    tf = tuple(l1)
    return tf

if __name__ == '__main__':

    length = int(input().strip())

    qw1 = []
    for i in range(4):
        qw2 = []
        for _ in range(length):
            qw2_item = int(input().strip())
            qw2.append(qw2_item)
        qw1.append(tuple(qw2))
    tupb = tuple(qw1)

    q = performIterator(tupb)
    print(q)
