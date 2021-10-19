import sqlite3
# establishing  a database connection
con = sqlite3.connect('D:\\TEST.db')
# preparing a cursor object
cursor = con.cursor()
# preparing sql statements
sql1 = 'DROP TABLE IF EXISTS EMPLOYEE'

sql2 = '''

       CREATE TABLE EMPLOYEE (
       EMPID INT(6) NOT NULL,
       NAME CHAR(20) NOT NULL,
       AGE INT,
       SEX CHAR(1),
       INCOME FLOAT
       )
      '''

# executing sql statements
cursor.execute(sql1)
cursor.execute(sql2)

# preparing sql statement
rec = (456789, 'Frodo', 45, 'M', 100000.00)
sql = '''
      INSERT INTO EMPLOYEE VALUES ( ?, ?, ?, ?, ?)
      '''

try:

    cursor.execute(sql, rec)

    con.commit()

except Exception as e:

    print("Error Message :", str(e))

    con.rollback()

# executing sql statement using try ... except blocks
records = [

    (123456, 'John', 25, 'M', 50000.00),

    (234651, 'Juli', 35, 'F', 75000.00),

    (345121, 'Fred', 48, 'M', 125000.00),

    (562412, 'Rosy', 28, 'F', 52000.00)

    ]

sql = '''

       INSERT INTO EMPLOYEE VALUES ( ?, ?, ?, ?, ?)

      '''
try:

    cursor.executemany(sql, records)

    con.commit()

except Exception as e:

    print("Error Message :", str(e))

    con.rollback()

# preparing sql statement
sql = '''
       SELECT * FROM EMPLOYEE
      '''
# executing the sql statement using `try ... except`
try:
    cursor.execute(sql)
except  Exception as e:
    print('Unable to fetch data.', str(e))
# fetching the records

records = cursor.fetchall()



# Displaying the records

#for record in records:

    #print(record)

#SELECT * FROM EMPLOYEE WHERE INCOME=10000.00
sql44 = '''
        SELECT * FROM EMPLOYEE 
        '''
        #WHERE INCOME=10000.00
try:
    cursor.execute(sql44)
except  Exception as e:
    print('Unable to fetch data.', str(e))

records44 = cursor.fetchall()
print(records44)
# closing the connection
con.close()