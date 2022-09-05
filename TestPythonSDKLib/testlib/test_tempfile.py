import os
import tempfile
import shutil


# Create a temporary working directory
TEMP = tempfile.mkdtemp(prefix="local_", suffix="_test")
print(TEMP)


# 动态写 Python 源码并执行
py_path = os.path.join(TEMP, 'cmd.py')
f = open(py_path, "w+")
f.write("print(f'hello world. {1+2+3}')")
f.flush()
f.close()

f = open(py_path, "r+")
exec(f.read())
f.close()


# Clean up our temporary working directory
if TEMP:
    shutil.rmtree(TEMP)


