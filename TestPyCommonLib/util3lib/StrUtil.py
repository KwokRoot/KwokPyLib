import re


# 删除字符串中 ascii 码的控制字符
def strip_ascii_ctl(input):
    return re.sub(r"[\x01-\x1F\x7F]", "", input)


