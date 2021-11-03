#!/bin/python3

import math
import os
import random
import re
import sys
import calendar
import datetime

 

def dateandtime(val,tup):
    l1=[]
    s=""
    if(val==1):
        for x in tup:
            s+=str(x)

        d1 = datetime.datetime.strptime(s,'%Y%m%d').date()
        l1.append(d1)
        l1.append(datetime.date.strftime(d1,'%d/%m/%Y'))
    elif(val==2):
        l1.append(datetime.date.fromtimestamp(tup[0]))
    elif(val==3):
        s = ''
        for x in tup:
            s+=str(x)
        s1=int(s)
        t = datetime.time(tup[0],tup[1],tup[2])
        l1.append(t)
        h=datetime.time.strftime(t,'%I')

        l1.append(h)
    elif(val==4):
        for x in tup:
            s+=str(x)
        s1=int(s)
        d1 = datetime.date(tup[0],tup[1],tup[2])
        l1.append(calendar.day_name[d1.weekday()])
        l1.append(calendar.month_name[d1.month])
        l1.append(str(d1.strftime('%j')))
    elif(val==5):
        s=''
        for x in tup:
            s+=str(x)
        s1=int(s)
        l1.append(datetime.datetime.strptime(s,'%Y%m%d%H%M%S'))
    return l1

if __name__ == '__main__':
    val = int(input().strip())
    
    if val ==1 or val==4 or val ==3:
        qw1_count=3
    if val==2:
        qw1_count=1
    if val ==5:
        qw1_count=6
    qw1 = []

    for _ in range(qw1_count):
        qw1_item = int(input().strip())
        qw1.append(qw1_item)
        
    tup=tuple(qw1)
    
    ans = dateandtime(val,tup)
    
    print(ans)