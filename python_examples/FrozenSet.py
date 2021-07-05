# https://www.programiz.com/python-programming/methods/built-in/frozenset
# https://stackoverflow.com/questions/50871370/python-sets-difference-vs-symmetric-difference

vowels = {'a','e','i','o','u'}

fset = frozenset(vowels)

try:
    fset.add('dont add')
except:
    print(" cannot add to frozenset")

print(" fset -> ", fset)

for i in fset:
    print(" i -> ", i)

hm = {0:1}
fsetKeys = frozenset(hm)
print(" fset1 -> ", fsetKeys)

fsetValues = frozenset(hm.values())
print(fsetValues)

fset1 = frozenset([1,2,3])
fset2 = frozenset([4,5,6,1,2])

print(" fset union -> ", fset1.union(fset2))
print( " fset intersection fset2 -> ", fset1.intersection((fset2)))

print( " fset intersection fset2 -> ", fset1.difference((fset2)), fset2.difference(fset1))

print(" fset symetric difference i.e. Elements exactly in one set -> ", fset1.symmetric_difference(fset2))

set1 = set([1,2,3])
set2 = set([4,5,6,1,2])
print(" set symetric difference i.e. Elements exactly in one set -> ", set1.symmetric_difference(set2))


