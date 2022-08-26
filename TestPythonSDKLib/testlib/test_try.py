try:
    print("执行的代码")
    # raise FileExistsError("自定义抛异常")

except Exception as e:
    print("有异常异常执行的代码")
    # exit(-1)

else:
    print("无异常执行的代码")

finally:
    print("有无异常都会执行的代码")

print("END")
