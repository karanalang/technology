# SortedList ->
# http://www.grantjenks.com/docs/sortedcontainers/implementation.html
# http://www.grantjenks.com/docs/sortedcontainers/index.html

from sortedcontainers import SortedList, SortedDict

sl = SortedList(['a','z','b','d','p','q','r'])
print(" sl -> ", sl, " sl[-2:] -> ", sl[-2:])

sl.pop(0)
print(" after pop(0) -> ", sl)


# sl*=10
print(" sl -> ", sl)
print(" count of a in sl -> ", sl.count('a'))


# sd = SortedDict({1:'1', 5:'5', 3:'3', 10:'10', 7:'7'})
# print("sd -> ", sd)