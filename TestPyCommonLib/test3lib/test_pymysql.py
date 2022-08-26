import pymysql

conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", password="123456", database="quartz", cursorclass=pymysql.cursors.SSDictCursor)
cursor = conn.cursor()

cursor.execute("SELECT * FROM quartz.qrtz_triggers")


# cursor.execute("delete  from quartz.qrtz_fired_triggers")
## 提交事务
# conn.commit()
# print(cursor.rowcount)


# 获取表头
# desc = cursor.description
# print("表头:", ",".join([item[0] for item in desc]))


# print(cursor)

result = cursor.fetchall()
print(len(result))

cursor.close()
conn.close()

