# https://stackoverflow.com/questions/3954530/how-to-make-heapq-evaluate-the-heap-off-of-a-specific-attribute

import heapq

def new_cmp_lt(self, a, b):
    return a[1]<b[1]

heapq.cmp_lt = new_cmp_lt

pq = [(1, 3), (-2, 1), (6,7)]

heapq.heapify(pq)

while pq:
    print(heapq.heappop(pq))


