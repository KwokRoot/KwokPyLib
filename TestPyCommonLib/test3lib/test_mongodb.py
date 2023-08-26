import pymongo

# mongodb://root:123456@127.0.0.1:27017/?authSource=admin
# timeoutMS 整个操作的超时时间
# serverSelectionTimeoutMS、connectTimeoutMS、socketTimeoutMS 各步操作的超时时间。具体使用时见源码注释。

client = pymongo.MongoClient("mongodb://root:123456@127.0.0.1:27017/?authSource=admin",
                             timeoutMS=10000)
db = client["local"]
col = db["db.user"]

# find = {"create_at": {"$lte": 1657900800000}}
find = {}
sort = [("name", pymongo.ASCENDING)]
skip = 0
limit = 10


# 增
ls = [
    {"_id": 1, "name": "Baidu", "address": "百度"},
    {"_id": 2, "name": "Alibaba", "address": "阿里巴巴"},
    {"_id": 3, "name": "Tencent", "address": "腾讯"},
    {"_id": 4, "name": "Google", "address": "Google 搜索"}
]
try:
    x = col.insert_many(ls)
    # 输出插入的所有文档对应的 _id 值
    print(x.inserted_ids)
except Exception as e:
    print(e)


# count
doc_count = col.count_documents(find, skip=skip)
print(f">>> 删除前文档数：{doc_count}")


# # 删：
r = col.delete_many({"name": "Google"})
print(f"=== 删除的文档数：{r.deleted_count}")


# 改
r = col.update_many({"_id": 1}, {"$set": {"_id": 1, "name": "JD", "cn_name": "京东"}})
print(f"=== 更新的文档数：{r.matched_count}")


# 查
rs = col.find(find).skip(skip).limit(limit).sort(sort)

for r in rs:
    print(r)


# count
doc_count = col.count_documents(find, skip=skip)
print(f">>> 删除后文档数：{doc_count}")


# 索引
# ## 创建索引
col.create_index([("name", 1)], name="name_index")

# ## 创建全文索引
col.create_index([("name", "text")], name="index_all")
# col.create_index([("$**", "text")])

# ## 全文检索
# cursor = col.find({"$text": {"$search": "Kwok"}})

# ## 删除索引
print(list(col.list_indexes()))
col.drop_indexes()
print(list(col.list_indexes()))


# 删除集合
db.drop_collection("db.user")

# 关闭客户端
client.close()


