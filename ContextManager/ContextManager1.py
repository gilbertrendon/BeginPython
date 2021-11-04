import sys
import os
import inspect
from contextlib import contextmanager
# Complete the function below.
@contextmanager
def writeto(filename, input_text):
    with open(filename, 'wb') as target:
        target.write(input_text)
    yield
    file = open(filename, "w")
    file.write(input_text)
    file.close() #This close() is important

if __name__ == "__main__":
    try:
        filename = str(input())
    except Exception as e:
        filename = None
        print("Filename :",filename,e, str(e))

    try:
        input_text = str(input())
    except Exception as e:
        input_text = None
        print("input_text :",input_text,e, str(e))

    res = writeto(filename, input_text)
    
    if 'with' in inspect.getsource(writeto):
        print("'with' used in 'writeTo' function definition.")
        
    if os.path.exists(filename):
        print('File :',filename, 'is present on system.')
        with open(filename) as fp:
            content = fp.read()
        if content == input_text:
            print('File Contents are :', content)
    
import sys
import os
import inspect
from contextlib import contextmanager

with open(filename, 'w') as target:
    target.write(input_text)
#yield
# Complete the function below.
@contextmanager
def writeto(filename, input_text):
    file = open(filename, "w")
    file.write(input_text)
    file.close() #This close() is important



if __name__ == "__main__":
    try:
        filename = str(input())
    except Exception as e:
        filename = None
        print("Filename :",filename,"Error Message :", str(e))

    try:
        input_text = str(input())
    except Exception as e:
        input_text = None
        print("input_text :",input_text,"Error Message :", str(e))

    res = writeto(filename, input_text)
    
    if 'with' in inspect.getsource(writeto):
        print("'with' used in 'writeTo' function definition.")
        
    if os.path.exists(filename):
        print('File :',filename, 'is present on system.')
        with open(filename) as fp:
            
            content = fp.read()
        if content == input_text:
            print('File Contents are :', content)
    





