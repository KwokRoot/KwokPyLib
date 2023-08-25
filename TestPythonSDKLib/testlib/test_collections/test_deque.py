from collections import deque

# deque 双端队列
# 定义队列长度
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)

q.appendleft(0)
print(q)

q.append(6)
print(q)

q2 = deque([6, 7, 8, 9])
q2.extendleft(q)
print(q2)


# 队列旋转
q2.rotate(3)
print(q2)
q2.rotate(-3)
print(q2)


# 某元素个数
print(q2.count(6))


