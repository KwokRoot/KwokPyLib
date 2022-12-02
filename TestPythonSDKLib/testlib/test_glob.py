import glob


# 文件通配符查找
file_list = glob.glob(r"F:\opt\test*.txt", recursive=True)
print(file_list)


