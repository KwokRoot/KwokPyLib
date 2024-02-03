# pip install pypinyin
from pypinyin import pinyin, lazy_pinyin, Style


hz = '你好，世界！'
pinyin_list = pinyin(hz)
print(pinyin_list)


pinyin_str_list = lazy_pinyin(hz)
print(pinyin_str_list)


# 声母
pinyin_initials = pinyin('拼音', style=Style.INITIALS, strict=False)
print(pinyin_initials)

# 无声调
pinyin_normal = pinyin('拼音', style=Style.NORMAL)
print(pinyin_normal)

# 普通声调
pinyin_tone = pinyin('拼音', style=Style.TONE)
print(pinyin_tone)

# 数字声调
pinyin_tone2 = pinyin('拼音', style=Style.TONE2)
print(pinyin_tone2)

