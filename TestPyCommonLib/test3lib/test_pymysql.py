import pymysql

# 连接数据库
conn = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='root',
                       password='123456',
                       database='test',
                       cursorclass=pymysql.cursors.DictCursor)

# 执行查询
cursor = conn.cursor()
sql = "SELECT `id`, `password` FROM `user`"
cursor.execute(sql)

# 获取结果头信息
desc = cursor.description
print("头信息:", ", ".join([item[0] for item in desc]))

# 查询所有
result = cursor.fetchall()
print(len(result))
for r in result:
    print(r)


with conn:
    with conn.cursor() as cursor:
        sql = """
               CREATE TABLE `user` (
                 `id` bigint(20) NOT NULL AUTO_INCREMENT,
                 `email` varchar(255) DEFAULT NULL,
                 `password` varchar(255) DEFAULT NULL,
                 PRIMARY KEY (`id`)
               ) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4;
           """
        try:
            cursor.execute(sql)
        except Exception as e:
            print(e)
            pass

    with conn.cursor() as cursor:
        sql = "INSERT INTO `user` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('kwok@123.com', 'pw'))
        # 提交事务，connection is not autocommit by default. So you must commit to save.
        conn.commit()
        print(cursor.rowcount)

    with conn.cursor() as cursor:
        sql = "SELECT `id`, `password` FROM `user` WHERE `email` like %s"
        cursor.execute(sql, ("%@123.com%",))

        result = cursor.fetchmany(size=10)
        print(result)

# cursor.close()
# conn.close()

