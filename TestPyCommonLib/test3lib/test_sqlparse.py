# pip install sqlparse

"""
Python SQL 格式化、解析工具 `sqlparse` .
"""

import sqlparse

sql_str = """
select * from (select CASE when spent_time >= 0 and spent_time < 1000 THEN "0-1000" when spent_time>= 1000 THEN "1000-*" END AS `key`, count(1) AS doc_count from t_test where (o_l_time >= '2025-08-08 00:00:00.000000') AND (o_l_time <= '2025-08-08 23:59:59.999999') AND kfk_topic = 'test' AND CASE when spent_time >= 0 and spent_time < 1000 THEN "0-1000" when spent_time>= 1000 THEN "1000-*"END IS NOT NULL GROUP BY CASE when spent_time >= 0 and spent_time < 1000 THEN "0-1000" when spent_time>= 1000 THEN "1000-*" END) T  ORDER BY CASE when "0-1000" THEN "1" when "1000-*" THEN "2-*" END
"""

sql_str = sql_str.strip()

# sql 格式化
formatted = sqlparse.format(
    sql_str,
    reindent=True,
    keyword_case='upper',
    strip_comments=True,
    use_space_around_operators=True
)

print(formatted)


print("---" * 36)
# sql 解析
parsed = sqlparse.parse(sql_str)
for token in parsed[0].tokens:
    print(token.ttype, token.value)

