
import math
import os
import random
import re
import sys



#
# Complete the 'Bank_ATM' function below.
#
# Define the Class for user-defined exceptions "MinimumDepositError" and "MinimumBalanceError" here






class MinimumDepositError(Exception):
    pass
class MinimumBalanceError(Exception):
    pass
def Bank_ATM(balance,choice,amount):

    if(balance<500):
        raise ValueError("As per the Minimum Balance Policy, Balance must be at least 500")
    if(choice == 1 and amount<2000):
        raise MinimumDepositError("The Minimum amount of Deposit should be 2000.")
    elif(choice == 1):
        balance+=amount
        print("Updated Balance Amount:  "+str(balance))

    if(choice == 2 and balance-amount<500):
        raise MinimumBalanceError("You cannot withdraw this amount due to Minimum Balance Policy")
    elif(choice ==2):
        balance-=amount
        print("Updated Balance Amount:  "+str(balance))

if __name__ == '__main__':
    
    bal = int(input())
    ch = int(input())
    amt = int(input())
    
    try:
        Bank_ATM(bal,ch,amt)
    
    
    except ValueError as e:
        print(e)
    except MinimumDepositError as e:
        print(e)
    except MinimumBalanceError as e:
        print(e)