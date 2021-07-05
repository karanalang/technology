s1 = set([1, 2, 3, 5])
print(" discard -> does not throw exception when element is not present in set ")
s1.discard(7)

s1.discard(3)

print(s1)

try:
    s1.remove(3)
except:
    print(" exception in removing item from set ")
