import math
import os
import random
import re
import sys
#
# Complete the 'encrdecr' function below.
#
# The function is expected to return a LIST.
# The function accepts following parameters:
#  1. STRING keyval
#  2. STRING textencr
#  3. Byte-code textdecr
#
from cryptography.fernet import Fernet
def encrdecr(keyval, textencr, textdecr):

    l1=[]
    f=Fernet(keyval)
    l1.append(f.encrypt(textencr))
    l1.append(f.decrypt(textdecr).decode())
    print(l1)
    return l1
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
 
    file = open('key.key', 'rb')#Toca ver donde busca, puede ser en la misma carpeta de este archivo
    key = file.read()  # The key will be type bytes
    file.close()
    
    keyval = key

    textencr = str(input()).encode()

    textdecr = str(input()).encode()


    result = encrdecr(keyval, textencr, textdecr)
    bk=[]
    f = Fernet(key)
    val = f.decrypt(result[0])
    bk.append(val.decode())
    bk.append(result[1])

    #fptr.write(str(bk) + '\n')

    #fptr.close()
