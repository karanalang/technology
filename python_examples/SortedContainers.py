# http://www.grantjenks.com/docs/sortedcontainers/

'''
sorted containers proveides -> sortedlist, sorteddict, SortedSet
'''

from collections import defaultdict
from sortedcontainers import SortedDict, SortedList, SortedSet


hm = {1:1, 2:2, 3:3, 4:4}

sorted_hm = SortedDict(hm)
print(" sorted_hm -> ", sorted_hm)

# sorted_hm.update(1,2.75)
#
# print(" after update -> ", sorted_hm)

for i in sorted_hm:
    print(" in sorted_hm -> ", i)


sl = SortedList([6,7,1,4,9])
print(" sortedList  -> ", sl)

ss = SortedSet()
ss.add(2)
ss.add(1)
ss.add(10)
ss.add(0.5)

print(" sortedSet -> ", ss)
for n in ss:
    print(" n -> ", n)




