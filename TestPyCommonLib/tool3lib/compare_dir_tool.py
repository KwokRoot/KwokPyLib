import os
from datetime import datetime


# By KwokRoot
# At 2023-05-06
def main():
    compare(r"F:\Kwok\Favorites\MP3", r"I:\我的收藏\音乐MP3")


def compare(root_dir1, root_dir2):

    # 获取两目录中所有文件属性元组的集合
    dir1_name_size_mtime_set = walk_dir_file_arr_func(root_dir1)
    dir2_name_size_mtime_set = walk_dir_file_arr_func(root_dir2)

    # 获取两目录不同文件
    dir1_dir2_diff_set = dir1_name_size_mtime_set - dir2_name_size_mtime_set
    dir2_dir1_diff_set = dir2_name_size_mtime_set - dir1_name_size_mtime_set

    # 转化为文件名-文件属性元组 的 字典
    dir1_dir2_diff_dict = {l[0]: l for l in dir1_dir2_diff_set}
    dir2_dir1_diff_dict = {l[0]: l for l in dir2_dir1_diff_set}

    # 转化为文件名集合
    dir1_dir2_diff_file_name_set = set([l[0] for l in dir1_dir2_diff_set])
    dir2_dir1_diff_file_name_set = set([l[0] for l in dir2_dir1_diff_set])

    print("*" * 6 + " dir1、dir2 变更文件列表 " + "*" * 6)

    # 属性有变更的文件，即两目录中文件属性元组不同，文件名相同的集合
    diff_file_name_set = dir1_dir2_diff_file_name_set & dir2_dir1_diff_file_name_set
    for i, l in enumerate(sorted(diff_file_name_set)):
        # 文件大小一样时，忽略差异，可选
        if dir1_dir2_diff_dict.get(l)[1] != dir2_dir1_diff_dict.get(l)[1]:
            if dir1_dir2_diff_dict.get(l)[2] > dir2_dir1_diff_dict.get(l)[2]:
                print(i + 1, os.path.join(root_dir1, l), dir1_dir2_diff_dict.get(l), " << [*新*] <-- ",
                      os.path.join(root_dir2, l), dir2_dir1_diff_dict.get(l))
            else:
                print(i + 1, os.path.join(root_dir1, l), dir1_dir2_diff_dict.get(l), " --> [*新*] >> ",
                      os.path.join(root_dir2, l), dir2_dir1_diff_dict.get(l))

    print("\n", "=*=" * 36, "\n")

    print("*" * 9 + " dir1 独有文件列表 " + "*" * 9)
    # dir1 独有文件列表
    for l in sorted(dir1_dir2_diff_file_name_set - diff_file_name_set):
        file_name_size_mtime_tuple = dir1_dir2_diff_dict.get(l)
        print(os.path.join(root_dir1, file_name_size_mtime_tuple[0]), file_name_size_mtime_tuple[1], file_name_size_mtime_tuple[2])

    print("\n", "=*=" * 36, "\n")

    # dir2 独有文件列表
    print("*" * 9 + " dir2 独有文件列表 " + "*" * 9)
    for l in sorted(dir2_dir1_diff_file_name_set - diff_file_name_set):
        file_name_size_mtime_tuple = dir2_dir1_diff_dict.get(l)
        print(os.path.join(root_dir2, file_name_size_mtime_tuple[0]), file_name_size_mtime_tuple[1], file_name_size_mtime_tuple[2])


# 遍历目录，返回 (文件相对路径、文件大小、文件修改时间)
def walk_dir_file_arr_func(root_dir):
    file_name_size_mtime_set = set()
    for root, dirs, files in os.walk(root_dir):
        root_dir_len = len(root_dir) + 1
        if files:
            for file in files:
                file_path = os.path.join(root, file)
                file_info = os.stat(file_path)
                file_size = file_info.st_size
                file_mtime = datetime.fromtimestamp(file_info.st_mtime).strftime("%Y-%m-%d %H:%M:%S.%f")
                # print({file_path[root_dir_len:]}, {file_size}, {file_mtime})
                file_name_size_mtime_set.add((file_path[root_dir_len:], file_size, file_mtime))
    return file_name_size_mtime_set


if __name__ == '__main__':

    # dir_name_size_mtime_set = walk_dir_file_arr_func(r"D:\opt")
    # print(dir_name_size_mtime_set)

    main()

