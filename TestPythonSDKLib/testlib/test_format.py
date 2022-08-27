
# 重复字符串的便捷方式 及 字符串格式化的便捷方式：
print("=" * 36)
print("总计: %s" % len(range(3)))
print("=" * 36)

# 拓展：
# 字符串格式化其他2种格式：

# Python2.6+ 可使用 `str.format()`。format() 函数中大括号 `{}`、 `:` 作为特殊字符代替 `%`
print("总计: {}".format(len(range(6))))

# f-string` - Python3.6+ 引入的字符串格式化。(推荐)
print(f"总计: {len(range(9))}")

