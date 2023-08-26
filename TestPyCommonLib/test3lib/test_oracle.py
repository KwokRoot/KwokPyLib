# pip install cx-Oracle
import cx_Oracle


# 设置 Oracle Client library 路径
cx_Oracle.init_oracle_client(r"D:\oracle\instantclient-basiclite-windows.x64-11.2.0.4.0\instantclient_11_2")

# 账号、密码、服务器
db = cx_Oracle.connect(user="", password="", dsn="10.10.86.101:1521/test")

# 创建游标
cursor = db.cursor()

# 查询 SQL
sql = "SELECT * FROM USER WHERE STATUS='1' ORDER BY ID ASC"

# 查询 Oracle 版本
# sql = "select * from v$version"

# 执行语句
cursor.execute(sql)

# 获取标题
fields = [field[0] for field in cursor.description]
for field in fields:
    print(field, sep=", ")

# 获取结果
rows = cursor.fetchall()
for row in rows:
    print(row)
    print("{0}, {1}, {2}".format(row[0], row[1], row[2]))

# 关闭游标
cursor.close()

# 关闭连接
db.close()


