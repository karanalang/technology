# https://www.geeksforgeeks.org/python-set-operations-union-intersection-difference-symmetric-difference/

s1 = set([1,2,34,7])
s2 = set([7,8,9,1])

print(" intersections of sets -> ", (s1 & s2))
print(" Union of sets -> ", (s1|s2))
print(" Difference of sets -> ", (s1-s2))
print(" Symetric difference i.e. (s1-s2) | (s2-s1) -> ", (s1^s2), " symetric diff again -> ", (s1-s2) | (s2-s1))

print(" Intersection s1.intersection(s2) -> ", s1.intersection(s2))
print(" s1.difference(s2) -> ", s1.difference(s2))
print(" s2.difference(s1) -> ", s2.difference(s1))
print(" s1.isdisjoint(s2) -> ", s1.isdisjoint(s2))

s3 = set([1,2])
s4 = set([1,2,3,4,7])

print(" issubset -> ", s3.issubset(s4))
print(" isSuperSet -> ", s3.issuperset(s4))

