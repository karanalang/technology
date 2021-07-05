import heapq

l = [[0, 0, 2]]
heapq.heapify(l)

heapq.heappush(l, [2, 1, 0])

heapq.heappush(l, [1, 3, 1])

print(" heapified l -> ", l)

while len(l) > 0:
    item = heapq.heappop(l)
    print(" item -> ", item)




