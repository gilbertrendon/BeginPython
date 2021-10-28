import math
import os
import random
import re
import sys



#
# Complete the 'Library' function below.
#

 
def Library(memberfee,installment,book):
    # print(memberfee,installment,book)
    
    if installment > 3:
        raise ValueError("Maximum Permitted Number of Installments is 3")
    
    elif installment == 0:
        raise ZeroDivisionError("Number of Installments cannot be Zero.")
    else:
        per = memberfee/installment
        
        print("Amount per Installment is  {}".format(per,'.1f'))
    hp = ['philosophers stone','chamber of secrets','prisoner of azkaban','goblet of fire','order of phoenix','half blood prince','deathly hallows 1','deathly hallows 2']
    if book.lower() in hp:
        print("It is available in this section")
    else:
        raise NameError("No such book exists in this section")

if __name__ == '__main__':
    
    memberfee = int(input())
    installment = int(input())
    book = input()
    
    try:
        Library(memberfee,installment,book)
        
    except ZeroDivisionError as e:
        print(e)
    except ValueError as e:
        print(e)
    except NameError as e:
        print(e)