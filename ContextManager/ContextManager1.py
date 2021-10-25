# import sqlite3
# try:
#     dbConnection = sqlite3.connect('TEST.db')
#     cursor = dbConnection.cursor()
#     '''
#     Few db operations
#     ...
#     '''
# except Exception:
#     print('No Connection.')
# finally:
#     dbConnection.close()
# import sqlite3
# class DbConnect(object):
#     def __init__(self, dbname):
#         self.dbname = dbname
#     def __enter__(self):
#         self.dbConnection = sqlite3.connect(self.dbname)
#         return self.dbConnection
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.dbConnection.close()
# with DbConnect('TEST.db') as db:
#     cursor = db.cursor()
#     '''
#    Few db operations
#    ...
#     '''
# from contextlib import contextmanager

# @contextmanager
# def tag(name):
#     print("<%s>" % name)
#     yield
#     print("</%s>" % name)

# with tag('h1') :
#     print('Hello')
# from contextlib import contextmanager

# @contextmanager
# def context():
#     print('Entering Context')
#     yield 
#     print("Exiting Context")

# with context():
#     print('In Context')

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
    

#ESTE FUE EL CÓDIGO QUE FUNCIONÓ
# import sqlite3
# try:
#     dbConnection = sqlite3.connect('TEST.db')
#     cursor = dbConnection.cursor()
#     '''
#     Few db operations
#     ...
#     '''
# except Exception:
#     print('No Connection.')
# finally:
#     dbConnection.close()
# import sqlite3
# class DbConnect(object):
#     def __init__(self, dbname):
#         self.dbname = dbname
#     def __enter__(self):
#         self.dbConnection = sqlite3.connect(self.dbname)
#         return self.dbConnection
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.dbConnection.close()
# with DbConnect('TEST.db') as db:
#     cursor = db.cursor()
#     '''
#    Few db operations
#    ...
#     '''
# from contextlib import contextmanager

# @contextmanager
# def tag(name):
#     print("<%s>" % name)
#     yield
#     print("</%s>" % name)

# with tag('h1') :
#     print('Hello')
# from contextlib import contextmanager

# @contextmanager
# def context():
#     print('Entering Context')
#     yield 
#     print("Exiting Context")

# with context():
#     print('In Context')

import sys
import os
import inspect
from contextlib import contextmanager
# Complete the function below.
@contextmanager
def writeto(filename, input_text):
    file = open(filename, "w")
    file.write(input_text)
    file.close() #This close() is important
    # with open(filename, 'wb') as target:
    #     target.write(input_text)
    # yield
    

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
    





