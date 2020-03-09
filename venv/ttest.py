import sqlite3

conn = sqlite3.connect('oj.db')
c = conn.cursor()
# c.execute('''CREATE TABLE if not exists administrator
#            (ID TEXT PRIMARY KEY     NOT NULL,
#            NAME           TEXT    NOT NULL,
#            PASSWORD       TEXT    NOT NULL);''')
# print ("Opened database successfully");
id='001'
name='老师1'
password = '123'
s = "insert into {} values ('{}', '{}', '{}')".format('administrator', id, name, password)
c.execute(s)
# conn.commit()
# print('insert successfully444')
# #
# cursor = c.execute("SELECT * from users where ID = '001'")
# for row in cursor:
#    print ("ID = ", row[0])
#    print ("NAME = ", row[1])
#    print ("ADDRESS = ", row[2])
#使用featchall获得结果集（list）
# s = "SELECT * from user where ID = '008'"
#
# values = c.execute(s).fetchall()


# values = cursor.fetchall()
# print(values) #result:[('1', 'Michael')]

print ("Operation done successfully");
conn.close()