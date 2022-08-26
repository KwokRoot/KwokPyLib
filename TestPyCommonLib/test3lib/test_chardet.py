# 判断文件编码
import chardet

with open(r'/opt/redis.txt', 'rb') as f:
    text = f.read(100)
    print(chardet.detect(text))

