import sys

s = '''中国'''
print(s.encode("utf-8"))
print(s.encode("unicode-escape"))
print(s.encode())
print(sys.getdefaultencoding())

