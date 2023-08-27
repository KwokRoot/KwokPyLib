# pip install mysql-connector-python
import mysql.connector.pooling

__config = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "123456",
    "database": "test"
}

try:
    pool=mysql.connector.pooling.MySQLConnectionPool(
        **__config,
        pool_size=10
    )
except Exception as e:
    print(e)
