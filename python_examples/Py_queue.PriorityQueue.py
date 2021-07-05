from queue import PriorityQueue
# import self

q = PriorityQueue()
q.put(31)

q.put(4)

# with self.mutex:
#     return self.queue[0]
print(" smallest element in PriorityQueue -> ", q[0])

while not q.empty():
    print(q.get(1))