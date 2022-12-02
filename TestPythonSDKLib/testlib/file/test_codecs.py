import codecs


# 读写文件
with codecs.open(r"F:\opt\test.txt", "r", encoding="utf-8") as f:
    print(f.read())


print("*" * 36)


look_utf8 = codecs.lookup("utf-8")
utf8_str = look_utf8.encode("中国")
print(utf8_str)
print(look_utf8.decode(utf8_str[0]))


print("*" * 36)


look_gbk = codecs.lookup("gbk")
gbk_str = look_gbk.encode("中国")
print(gbk_str)
print(look_gbk.decode(gbk_str[0]))

