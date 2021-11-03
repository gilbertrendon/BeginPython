import math
import os
import random
import re
import sys
from collections import OrderedDict

def collectionfunc(text1, dictionary1, key1, val1, deduct, list1):

    d1=text1.split(' ')
    d = {}
    for x in d1:
        if(x in d):
            d[x]=d[x]+1
        else:
            d[x]=1
    d2={}
    for a in (sorted(d)):
        d2[a]=d[a]
    print(d2)

    c=dictionary1

    for x in c.keys():
        if(x in deduct.keys()):
            c[x]=c[x]-deduct[x]

    for x in deduct.keys():
        if(x not in c.keys()):
            c[x]=0-deduct[x]

    a=dict(c)
    print(a)
    od=OrderedDict()
    for x in range(len(key1)):
        od[key1[x]]=val1[x]
    od.pop(key1[1])
    od[key1[1]]=val1[1]
    d=dict(od)
    print(d)

    df = {}
    df['odd']=[]
    df['even']=[]
    for i in list1:
        if(i%2==0):
            df['even'].append(i)
        else:
            df['odd'].append(i)
    print({k:v for k,v in df.items() if len(v)>0})

if __name__ == '__main__':
    from collections import Counter

    text1 = input()
    
    n1 = int(input().strip())
    qw1 = []
    qw2 = []
    for _ in range(n1):
        qw1_item = (input().strip())
        qw1.append(qw1_item)
        qw2_item = int(input().strip())
        qw2.append(qw2_item)
    testdict={}
    for i in range(n1):
        testdict[qw1[i]]=qw2[i]
    collection1 = (testdict)
    
    qw1 = []
    n2 = int(input().strip())
    for _ in range(n2):
        qw1_item = (input().strip())
        qw1.append(qw1_item)
    key1 = qw1
    
    qw1 = []
    n3 = int(input().strip())
    for _ in range(n3):
        qw1_item = int(input().strip())
        qw1.append(qw1_item)
    val1 = qw1

    n4 = int(input().strip())
    qw1 = []
    qw2 = []
    for _ in range(n4):
        qw1_item = (input().strip())
        qw1.append(qw1_item)
        qw2_item = int(input().strip())
        qw2.append(qw2_item)
    testdict={}
    for i in range(n4):
        testdict[qw1[i]]=qw2[i]
    deduct = testdict

    qw1 = []
    n5 = int(input().strip())
    for _ in range(n5):
        qw1_item = int(input().strip())
        qw1.append(qw1_item)
    list1 = qw1

    collectionfunc(text1, collection1, key1, val1, deduct, list1)
