zimport sys
import os
import io
import re

# Complete the function below.
def subst(pattern, replace_str, string):
    #susbstitute pattern and return it
    new_str = []
    for i in range(len(string)):
        new_str.append(string[i].replace(pattern,replace_str))
    
    print(new_str)
    return new_str

def main():
    addr = ['100 NORTH MAIN ROAD',
            '100 BROAD ROAD APT.',
            'SAROJINI DEVI ROAD',
            'BROAD AVENUE ROAD']
            
    #Create pattern Implementation here 
    
    #Use subst function to replace 'ROAD' to 'RD.',Store as new_address
    new_address = subst(' ROAD',' RD.', addr)
    return new_address

'''For testing the code, no input is required'''
if __name__ == "__main__":
    f = open(os.environ['OUTPUT_PATH'], 'w')

    res = main();
    f.write(str(res) + "\n")


    f.close()
#!/bin/python3

import sys
import os
import io
import re

# Complete the function below.
def subst(pattern, replace_str, string):
    #susbstitute pattern and return it
    new_str = []
    for i in range(len(string)):
        new_str.append(string[i].replace(pattern,replace_str))
    
    print(new_str)
    return new_str

def main():
    addr = ['100 NORTH MAIN ROAD',
            '100 BROAD ROAD APT.',
            'SAROJINI DEVI ROAD',
            'BROAD AVENUE ROAD']
            
    #Create pattern Implementation here 
    
    #Use subst function to replace 'ROAD' to 'RD.',Store as new_address
    new_address = subst(' ROAD',' RD.', addr)
    return new_address

'''For testing the code, no input is required'''
if __name__ == "__main__":
    f = open(os.environ['OUTPUT_PATH'], 'w')

    res = main();
    f.write(str(res) + "\n")


    f.close()
