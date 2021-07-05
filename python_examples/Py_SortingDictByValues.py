import operator
import collections

# https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value

class SortDict:


    def sortDictByValues(self, d):
        print('d -> ', d)
        sortedByValue = sorted(d, key=operator.itemgetter(1))
        print(' sorting by values -> ', sortedByValue)
        # sortedByKey = sorted(d, key=operator.itemgetter(0))
        # print(' sorting by key -> ', sortedByKey)



# s = SortDict()
# d = {'a':3, 'b':2, 'c':1}
# s.sortDictByValues(d)


x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(1))
sorted_y = sorted(x.items(), key=operator.itemgetter(0))
sorted_d = sorted(x.items())
sorted_d1 = sorted(x)

print(' sorted_x -> ', sorted_x)
print(' sorted_y -> ', sorted_y)
print(' sorted_d -> ', sorted_d)
print(' sorted_d1 -> ', sorted_d1)

# if you want output as dict
ordD =collections.OrderedDict(sorted_x)
print(" ordD -> ", ordD)

for i in ordD:
    print(" i -> ", i)
