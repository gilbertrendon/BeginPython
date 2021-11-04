import zipfile
import sys
import os
import inspect

# Define 'writeTo' function below, such that# it writes input_text string to filename.
def writeto(filename, text):
    with open(filename,'w') as fp:
        fp.write(text)
        
# Define the function 'archive' below, such that
# it archives 'filename' into the 'zipfile'
def archive(zfile, filename):
    with zipfile.ZipFile(zfile,'w') as myzip:
        myzip.write(filename)

if __name__ == "__main__":
    try:
        filename = str(input())
    except Exception as e:
            print('Error Message :', str(e))
        filename = None

    try:
        input_text = str(input())
    except Exception as e:
            print("Error Message :", str(e))
        input_text = None
        
    try:
        zip_file = str(input())
    except Exception as e:
            print("Error Message :", str(e))
        zip_file = None
        
    res = writeto(filename, input_text)
    
    if 'with' in inspect.getsource(writeto):
        print("'with' used in 'writeTo' function definition.")
        
    if os.path.exists(filename):
        print('File :',filename, 'is present on system.')
 
    res = archive(zip_file, filename)
    
    if 'with' in inspect.getsource(archive):
        print("'with' used in 'archive' function definition.")
        
    if os.path.exists(zip_file):
        print('ZipFile :',zip_file, 'is present on system.')    
    

