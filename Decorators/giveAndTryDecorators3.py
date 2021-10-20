import sys
import os



def bold_tag(text):
    
    def decorator(txt):
        return '<b>'+txt+'<b>'
    return decorator(text)

#Add greet function definition here


'''Check the Tail section for input/output'''

if __name__ == "__main__":
    #with open(os.environ['OUTPUT_PATH'], 'w') as fout:
    txt = input()
    res = bold_tag(txt)
    print(res)
    #    fout.write("{}".format(*res_lst))
