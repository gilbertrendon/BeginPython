
import sys
import os
import datetime as dt


#Add log function and inner function implementation here

def greet(msg):
    def log(*args):#Asumiendo que los decoradores van dentro de la función y no afuera
        msg = 'Accessed the function -\'greet\' with arguments ('+*args+',) {}'
        return msg
    return log
    

'''Check the Tail section for input/output'''

    

if __name__ == "__main__":
    with open(os.environ['OUTPUT_PATH'], 'w') as fout:
        res_lst = list()
        res_lst.append(greet(str(input())))
        fout.write("{}".format(*res_lst))
