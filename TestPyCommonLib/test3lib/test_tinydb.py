# pip install tinydb
from tinydb import TinyDB, Query, where

db = TinyDB('temp/tinydb.json')

# db.insert({'name': 'Alice', 'age': 30})
# db.insert_multiple([{'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}])

result = db.all()
print(result)

User = Query()
print(db.search(User["name"] == 'Bob'))

print(db.search(where('name') == 'Bob'))

db.close()

