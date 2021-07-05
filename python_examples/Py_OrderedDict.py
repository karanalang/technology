from collections import OrderedDict, Counter

od = OrderedDict()
od[2] = 2.2
od[1] = 1.2

for i in od:
    print(" i -> ", i)

print(" od -> ", od)
print(" pop last item  added - LIFO ")
item = od.popitem(last=True)
print(" 1. od -> ", od , " item -> ",item)


od[2]=3.1
od[4]=5.1
od[5]=6.1
od[6]=7.1
od[7]=8.1


print(" 3. od -> ", od)

# item2=od.popitem(last=False)
# print(" item2, FIFO  -> ", item2)

print(list(od))
item3=od.pop(2)
print(" item3 -> ", item3)

ctr = Counter([4, 4, 5, 7, 5, 9, 10, 10])
ctr1=sorted(ctr.items(), key=lambda x:x[1])

print(" ctr1 -> ", ctr1)

od_ctr= OrderedDict(ctr1)
print(" od_ctr -> ", od_ctr)

print(" type(ctr)  -> ", type(ctr), " type(ctr.item()) -> ", type(ctr.items()))