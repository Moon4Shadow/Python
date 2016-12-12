import mysql.connector

cnn = mysql.connector.connect( user = 'root', database = 'test', password = 'lh123root')
cursor=cnn.cursor()
try:
  '第一种：直接字符串插入方式'
  sql_insert1="insert into student (name, age) values ('orange', 20)"
  cursor.execute(sql_insert1)
  '第二种：元组连接插入方式'
  sql_insert2="insert into student (name, age) values (%s, %s)"
  #此处的%s为占位符，而不是格式化字符串，所以age用%s
  data=('shiki',25)
  cursor.execute(sql_insert2,data)
  '第三种：字典连接插入方式'
  sql_insert3="insert into student (name, age) values (%(name)s, %(age)s)"
  data={'name':'mumu','age':30}
  cursor.execute(sql_insert3,data)
  #如果数据库引擎为Innodb，执行完成后需执行cnn.commit()进行事务提交
  cnn.commit()
except mysql.connector.Error as e:
  print('insert datas error!{}'.format(e))
finally:
  cursor.close()
  cnn.close()