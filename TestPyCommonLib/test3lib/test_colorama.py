# pip install colorama
import colorama

'''
控制台打印彩色字体
'''

# 初始化
# colorama.init()
colorama.init(autoreset=True)

# 颜色设置
print(colorama.Fore.RED + "红色字")
print(colorama.Fore.YELLOW + "黄色字")
print(colorama.Fore.BLUE + "蓝色字")
print(colorama.Fore.GREEN + "绿色字")
print(colorama.Fore.CYAN + "天蓝色字")

print(colorama.Fore.RESET + "*" * 36)


# 背景设置
print(colorama.Back.RED + "红色背景字")
print(colorama.Back.YELLOW + "黄色背景字")
print(colorama.Back.BLUE + "蓝色背景字")
print(colorama.Back.GREEN + "绿色背景字")
print(colorama.Back.CYAN + "天蓝色背景字")

print(colorama.Style.RESET_ALL + "*" * 36)


# 样式设置
print(colorama.Style.BRIGHT + "粗体字")

# 综合示例
print(colorama.Fore.YELLOW + colorama.Back.BLACK + 'Hello, World!' + colorama.Style.RESET_ALL)

