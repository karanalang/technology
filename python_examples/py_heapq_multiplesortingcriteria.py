l = [(0,1,3), (0,2,10), (0,2,5), (-1,1, 9)]

# expected -> (-1,1,9), (0,1,3), (0,2,5), (0,2,10)
import heapq

heapq.heapify(l)

while l:
    item = heapq.heappop(l)
    print(" item -> ", item)