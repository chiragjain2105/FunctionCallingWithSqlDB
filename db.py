import MySQLdb

conn = MySQLdb.connect(host='localhost', database='fncalling', user='root', password='1234')

cursor = conn.cursor()
cursor.execute("select * from students")

students = cursor.fetchall()
cursor.close()
conn.close()
