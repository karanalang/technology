# https://docs.python.org/3/library/bisect.html
# https://www.tutorialspoint.com/bisect-array-bisection-algorithm-in-python

import bisect


# data = [1, 2, 3,4 ]
#
# idx = bisect.bisect(data, 2)
# print(" bisect.bisect(data, 2) i.e. get the idx to the RIGHT of the elem 2 -> ", idx)
#
# data.insert(idx, 100)
#
# print(" data after bisect and insert -> ", data)


# data = [0, 100, 300,405]
# idx = bisect.bisect_left(data, 405)
# print(" bisect.bisect(data, 3) i.e. get the idx to the LEFT of the elem 3 -> ", idx)
# data.insert(idx, 405)
# print(" data after bidect_left and insert -> ", data)


# data = [1, 2, 3,4]
# idx = bisect.bisect_right(data, 5)
# print(" bisect.bisect(data, 2) i.e. get the idx to the RIGHT of the elem 2 -> ", idx)
# data.insert(idx, 103)
# print(" data after bidect_left and insert -> ", data)

data = [0, 100, 300,405]
idx = bisect.insort_left(data, 400)
print(" bisect.bisect(data, 3) i.e. get the idx to the LEFT of the elem 3 -> ", idx)
# data.insert(idx, 405)
print(" data after insort_left and insert -> ", data)


data = [0, 100, 300,405]
bisect.insort_right(data, 400)
print(" bisect.bisect(data, 3) i.e. get the idx to the LEFT of the elem 3 -> ", data)


data = [0, 100, 300,405]
bisect.insort(data, 400)
print(" bisect.bisect(data, 3) i.e. get the idx to the LEFT of the elem 3 -> ", data)
