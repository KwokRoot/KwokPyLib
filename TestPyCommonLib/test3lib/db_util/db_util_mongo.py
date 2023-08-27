import pymongo

client = pymongo.MongoClient("mongodb://root:123456@127.0.0.1:27017/?authSource=admin",
                             connectTimeoutMS=10000)
db = client["my_db"]
col = db["app_info"]

# find = {"create_at": {"$lte": 1691496000000}}
find = {}
sort = [("name", pymongo.ASCENDING)]
skip = 0
limit = 10
