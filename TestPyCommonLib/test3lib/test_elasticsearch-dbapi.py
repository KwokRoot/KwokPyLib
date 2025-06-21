# elasticsearch-dbapi 实现了 DBAPI（PEP-249）和 SQLAlchemy 方言，使得能够通过 SQL 访问 elasticsearch 集群进行只读查询。
# 此库支持 Elasticsearch 7.X 版本。
# pip install elasticsearch-dbapi
from es.elastic.api import connect

## DBAPI 方式
conn = connect(host='192.168.1.110', port=9200, timeout=60, fetch_size=10, time_zone="Asia/Shanghai")
# # 连接信息
# print(conn.es.info())

cursor = conn.cursor()
cursor.execute(
    "select * from \"test.index_or_alias\""
)
# 列名
if cursor.description:
    columns = [col[0] for col in cursor.description]
    print(columns)
# 数据
for row in cursor:
    print(row)



# ## SQLAlchemy 方式

# from sqlalchemy.engine import create_engine
# from sqlalchemy import text
# # Suppress specific warnings
# import warnings
# from sqlalchemy.exc import SADeprecationWarning, SAWarning
#
# warnings.filterwarnings("ignore", category=SADeprecationWarning)
# warnings.filterwarnings("ignore", category=SAWarning,
#                         message=r".*supports_statement_cache.*")
#
# engine = create_engine("elasticsearch+http://:@192.168.1.110:9200/",
#                        connect_args={
#                            "http_compress": True,  # 启用压缩
#                            "timeout": 30,  # 超时设置
#                            "max_retries": 3,  # 失败重试
#                            "retry_on_timeout": True,  # 超时重试
#                            "supports_statement_cache": True
#
#                        },execution_options={
#                            "compiled_cache": False,
#                            "stream_results": True,
#                         },)
# rows = engine.connect().execute(text(
#     'select * from "test.index_or_alias" LIMIT 10'
# ))
# # 列名
# print([col for col in rows.keys()])
# # 数据
# for row in rows:
#     print(row)

