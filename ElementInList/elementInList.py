import sys
import os

#Write detecter implementation
def detecter(element):
    #Write isIn implementation   
    def isIn(element):
        # firstValue = False
        # secondValue = False
        # if(element == 30):
        #     firstValue = True
        # else:
        #     if(element == 45):
        #         SecondValue = True 
        return True#(firstValue,secondValue) 
    
    return isIn(element)

        
 
        
#Write closure function implementation for detect30 and detect45
if __name__ == "__main__":
    with open(os.environ['OUTPUT_PATH'], 'w') as fout:
        func_lst = [detect30, detect45]
        res_lst = list()
        lst = list(map(lambda x: int(x.strip()), input().split(',')))
        for func in func_lst:
            res_lst.append(func(lst))
        fout.write("{}\n{}".format(*res_lst))
