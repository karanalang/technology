from collections import deque

q = deque()

q.append(3)
q.append(2)
q.append(5)

while q :
    print(q.pop())