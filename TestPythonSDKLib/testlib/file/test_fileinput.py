import fileinput

# input()不传任何参数时，默认以 stdin 作为输入源
# for line in fileinput.input():
#     if str(line).strip() == "exit":
#         exit(0)
#     else:
#         print(line)



# 读取批量文件
# fileinput.filename()      当前被读取的文件名
# fileinput.filelineno()    当前文件中的行号
# fileinput.lineno()        已被读取的累计行号

# from glob import glob
# files 通配符模式：files=glob(r'F:\opt\*.txt')
with fileinput.input(files=[r'F:\opt\test.txt', r'F:\opt\test1.txt'], openhook=fileinput.hook_encoded("utf-8")) as f:
    for line in f:
        print(f'{fileinput.filename():>20} 第{fileinput.lineno()}行: {line}')



