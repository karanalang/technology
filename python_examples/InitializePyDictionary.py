d = {}
for i in range(10000):
    d[i] = None

print(d)

d1 = range(40000)
dict_fromkeys = dict.fromkeys(d1)

dict_fromset = dict.fromkeys(set(range(40000)))


print(" dict_fromkeys -> ", dict_fromkeys)
print(" dict_fromset -> ", dict_fromset)


#
# d = dict(itertools.izip(xrange(4000000), itertools.repeat(None)))
