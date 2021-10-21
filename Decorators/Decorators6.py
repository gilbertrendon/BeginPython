import os
import sys


def bold_tag(text):
    
    def decorator(txt):
        return '<b>'+txt+'</b>'
    return decorator(text)

def italic_tag(func):
    
    def inner(func):
        return '<i>'+func+'</i>'
        
    return inner(func)
    
#Add greet() implementation here
    
'''check Tail section below for input / output'''

if __name__ == "__main__":
    txt = input()
    res = bold_tag(txt)
    res2 = italic_tag(res)
    print(res2)