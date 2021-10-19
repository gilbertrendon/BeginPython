#!/bin/python3

import sys
import os
import sqlite3




# Complete the following function:

def main():
    conn = sqlite3.connect('SAMPLE.db')
    #create connection cursor
    cursor = conn.cursor()
    #create table ITEMS using the cursor
    sql2 = '''
        CREATE TABLE EMPLOYEE (
        item_id INT(6) NOT NULL,
        item_name CHAR(20) NOT NULL,
        item_description CHAR(50) NOT NULL,
        item_category CHAR(20) NOT NULL,
        quantity_in_stock INT(6) NOT NULL
        )
        '''
    #commit connection 
    try:
        cursor.execute(sql2)
        conn.commit()
    except Exception as e:
        print("Error Message :", str(e))
    #close connection
    conn.close()


'''To test the code, no input is required'''

if __name__ == "__main__":
    f = open(os.environ['OUTPUT_PATH'], 'w')

    res = main();
    f.write(str(res) + "\n")


    f.close()
