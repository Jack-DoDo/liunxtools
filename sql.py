import mysql.connector
from mysql.connector import errorcode

用户名 = "root"
数据库名 =" "

while True:
  try:
    密码 = input("输入MySQL的 root 密码:")
    mydb = mysql.connector.connect( host="localhost" , user=用户名 , passwd=密码 )
    print( mydb , '\n成功连接数据库')
    break
  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Password error")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

while True:
    print (' ')
    print ('***************************************')
    print ('*                                     *')
    print ('*             MySQL 管理              *')
    print ('*                                     *')
    print ('***************************************')
    print (' ')
    print ('1. 显示数据库')
    print ('2. 创建数据库')
    print (' ')
    comm = input(" 回复数字或 Q 退出:")
    if comm == "1":
      mycursor = mydb.cursor()
      mycursor.execute("SHOW DATABASES")
      for x in mycursor:
        print(x)
    elif comm == "2":
      数据库名 = input(" 输入数据库名:")
      mycursor = mydb.cursor()
      mycursor.execute("CREATE DATABASE " + 数据库名)
    elif comm == "Q" or comm == "q":
        break