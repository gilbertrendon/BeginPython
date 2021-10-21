import sys
import os



def average(a,b,c):
    floata = float(a)
    floatb = float(b)
    floatc = float(c)
    print(floata,floatb,floatc)
    def inner(*args, **kwdargs):
        print('rqwerqerqwerqwer')
        #str_template = "Accessed the function -'{}' with arguments {} {}".format(func.__name__,args,kwdargs)
        # return 'Accessed the function -\'average\' with arguments ('+
        # floata+','+floatb+','+floatc+')'+'\{\}'+(floata+floatb+floatc)/3
        print('Accessed the function -\'average\' with arguments ('+
        str(floata)+','+str(floatb)+','+str(floatc)+')'+'\{\}'+str((floata+floatb+floatc)/3))                                                                               
    return inner(floata,floatb,floatc)

#Add greet function definition here
'''Check the Tail section for input/output'''

if __name__ == "__main__":
    #with open(os.environ['OUTPUT_PATH'], 'w') as fout:
    res_lst = list()
    (a,b,c) = (map(lambda x: float(x.strip()), input().split(',')))
    res_lst.append(average(a,b,c))
    #print(res_lst)
    #    fout.write("{}".format(*res_lst))
