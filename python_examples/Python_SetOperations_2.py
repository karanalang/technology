s1 = set('abcd')
print(" s -> ", s1)

s2 = set(['a','b','c'])
s3 = set(['d','e','f', 'a'])

print(" combining elements of 2 sets")
print(" s2|s3 -> ", s2|s3)

print(" common between 2 sets i.e. intersection(&) -> ", (s2&s3), " using intersection -> ", (s2.intersection(s3)))

print(" difference between 2 sets i.e. in s2, but not in s3 -> ", (s2.difference(s3)), " in s3, but not in s2 -> ", (s3.difference(s2)))

