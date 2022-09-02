import happybase

conn = happybase.Connection('10.10.89.142', port=9090)


# 创建表
try:
    conn.create_table("user", {"cf": dict(), "cf_ex": dict()})
except Exception as e:
    print("表存在")
    print(e)
else:
    print("表创建")


print("*" * 36)


# 查看所有表
table_list = conn.tables();
for table in table_list:
    print(str(table, "utf-8"))
    pass

table = conn.table("user", False)

print("*" * 36)


# 增/改(rowKey)
table.put("row-001", {"cf:name": "user-01", "cf:age": "16"})
table.put("row-001", {"cf:name": "user-02", "cf:age": "18", "cf_ex:married": "false"})
table.put("row-002", {"cf:name": "user-03", "cf:age": "22"})

# 查
one_row = table.row("row-001")
print(one_row)

print("*" * 36)

# 删
table.delete("row-001", columns=["cf_ex:married"])
table.delete("row-002", columns=["cf"])


# 查
for row_key, col_families in table.scan():
    row_key_str = row_key.decode('utf-8')
    for col_key, col_value in col_families.items():
        col_key_str = col_key.decode('utf-8')
        col_value_str = col_value.decode('utf-8')
        print("行:{} 列:{} 值:{}".format(row_key_str, col_key_str, col_value_str))


# 删除表
# conn.delete_table("user", True)


