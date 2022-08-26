import re

txt = """
aaabbbccc
a1b2c3
123321
abc123
abcd1234
a1b2c3d4
"""

ls = txt.split("\n")
# print(len(ls))

p = re.compile("(?:[a-z]{1}\\d{1})+", re.I)


# match 全串匹配

for l in ls:
    m = p.match(l)
    if m:
        print(m.group(0))

    m2 = re.match(p, l)
    if m2:
        print(m2.group())


# find 遍历匹配

p2 = re.compile("[a-z]{2}\\d{1}", re.I)
print(len(p2.findall(txt)))

fs = p2.finditer(txt)
for f in fs:
    print(f.group())

