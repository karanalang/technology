from collections import deque

dq = deque()
dq.append([0,0,0])
dq.append([1,1,1])
dq.append([2,2,2])


print(" deque -> ", dq)
while dq:
    [a,b,c] = dq.popleft()
    print(a, " - ", b, " - ", c)


dq1 = deque()
for i in range(5):
    dq1.append(i)

print(" dq1 -> ", dq1)

for i in range(len(dq1)):
    print(" dq1[i] -> ", dq1[i])