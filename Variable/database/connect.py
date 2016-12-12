import mysql.connector
cnn = mysql.connector.connect( user = 'root', database = 'test', password = 'lh123root')
sql_create_table = 'CREATE TABLE `student` ( \
`id` int(10) NOT NULL AUTO_INCREMENT, \
`name` varchar(10) DEFAULT NULL, \
`age` int(3) DEFAULT NULL,  PRIMARY KEY (`id`) \
)ENGINE = InnoDB DEFAULT CHARSET = utf8'
cursor = cnn.cursor()
try:
  cursor.execute(sql_create_table)
except mysql.connector.Error as e:
  print('create table orange fails!{}'.format(e))