import math
import os
import random
import re
import sys

def stringmethod(para, special1, special2, list1, strfind):
    word1=para
    for i in special1:
        word1=word1.replace(i,'')
    word2=word1[0:70]
    word2=word2[-1:-71:-1]
    print(word2)
    l=special2.join(list(word2.replace(" ",'')))
    print(l)
    count=0
    for i in list1:
        if (i in para):count+=1
    if count==len(list1):
        print("Every string in",list1,"were present")
    else:print("Every string in",list1,"were not present")
    print(word1.split()[0:20])
    list2=list()
    freq=[]
    for i in word1.split(" "):
        if word1.count(i)<13:
            if i in freq:pass
            else:freq.append(i)
    list2=freq[-1:-21:-1]
    print(list2[-1:-21:-1])
    print(word1.rindex(strfind))
  

if __name__ == '__main__':
    para = input()

    spch1 = input()

    spch2 = input()
    
    qw1_count = int(input().strip())

    qw1 = []

    for _ in range(qw1_count):
        qw1_item = input()
        qw1.append(qw1_item)

    strf = input()

    stringmethod(para, spch1, spch2, qw1, strf)
