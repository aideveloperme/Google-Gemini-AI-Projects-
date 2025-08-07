import sqlite3

##connect to sqlite3
connection=sqlite3.connect("student.db")

## creat a cursor object to insert record,create table,retrieve

cursor=connection.cursor();

##create the table

table_info ="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARK INT);
"""
cursor.execute(table_info)


##insert somemore records

cursor.execute('''insert into STUDENT values('Arish','Data Science','A',100)''')
cursor.execute('''insert into STUDENT values('Megh','Data Science','B',90)''')
cursor.execute('''insert into STUDENT values('Darish','Data Science','A',80)''')
cursor.execute('''insert into STUDENT values('krish','Data Science','C',60)''')
cursor.execute('''insert into STUDENT values('kiran','Data Science','D',30)''')

##display all records
print("the inserted recrods are")
data = cursor.execute('''select * From STUDENT''')

for row in data:
    print(row)

##close the connection 

connection.commit()

connection.close()