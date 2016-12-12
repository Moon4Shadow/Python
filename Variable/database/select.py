import mysql.connector
import urllib

cnn = mysql.connector.connect( user = 'root', database = 'test', password = 'lh123root')
cursor = cnn.cursor()
sql_insert1="select * from student"
ret = cursor.execute(sql_insert1)
for x in cursor:
    print(x)