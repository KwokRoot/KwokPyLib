from hashlib import md5, sha1

# md5
md5_obj = md5("admin".encode("utf-8"))
print(md5_obj.hexdigest())

# sha1
sha1_obj = sha1("admin".encode("utf-8"))
print(sha1_obj.hexdigest())

