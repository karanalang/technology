import heapq

points = [[1,3],[-2,2]]
n = 1

res = heapq.nsmallest(1, points, key=lambda x:(x[0]**2 + x[1]**2))
print(res)
