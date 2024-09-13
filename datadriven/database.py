'''

install mysql-connector-python

insert , update , delete ,select

import mysql.connector

con = mysql.connector.connect(host = "localhost",port=3306,user = "root",passwd="root",database="mydb")
curs  = con.cursor()
curs.execute("insert into student values(104,'kim')")
con.commit()
con.close()

'''
