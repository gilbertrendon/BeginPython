import sys
import os

#Write detecter implementation
def detect30(element):
    #Write isIn implementation
    #print(element)   
    
    def asdf(elem):
        if elem == 30:
            return True
        else:
            return False  
    def asdf(elem,elam):
        if elem == 30:
            return True
        else:
            return False         
    return asdf(element)

def detect45(element):
    #Write isIn implementation   
    #print(element)   
    def qwer(elem):
        if elem == 45:
            return True
        else:
            return False         
    return qwer(element)  
      
#Write closure function implementation for detect30 and detect45
if __name__ == "__main__":
    #print('Begining code')
    #with open(os.environ['OUTPUT_PATH'], 'w') as fout:
    func_lst = [detect30, detect45]
    res_lst = list()
    lst = list(map(lambda x: int(x.strip()), input().split(',')))
    for func in func_lst:
        res_lst.append(func(lst))

    firstbool = False
    for i in lst:
        firstbool = detect30(i)
        if(firstbool):
            break
    print(firstbool)
    secondbool = False
    for i in lst:
        secondbool = detect45(i)
        if(secondbool):
            break
    print(secondbool)
    #fout.write("{}\n{}".format(*res_lst))
