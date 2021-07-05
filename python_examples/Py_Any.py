# https://beginnersbook.com/2019/03/python-any-function/
# take an iterable - list, tuple, disctionary etc and returns true if any of the elements in the list is true,
# else returns false

print("ANY() WITH LISTS")

l = [1, 2, 3, 4]

print(" any(l) -> ", any(l))

l1 = [2, False, True]
print(any(l1))

l2 = [0,10, 20 ]
print(any(l2))

l3 = [0, False]
print(any(l3))

l4 = []
print(any(l4))

print("ANY() WITH DICTIONARIES")

# checks only the keys, not the values
d = {0:'1', 1:'2'}
print(any(d))

d1 = {0:'1', True:'2'}
print(any(d1))

d2 = {}
print(any(d2))

d3 = {'0':False}
print(any(d3))

print("ANY() WITH TUPLES")

t = (1, 0, 'Hello')
print(" any(t) -> ", any(t))

t1 = (0, 0, 'False')
print(" any(t1) -> ", any(t1))

t2 = (0, 0, False)
print(" any(t2) -> ", any(t2))

t3 = ()
print(" any(t3) -> ", any(t3))

t4 = (1, 3, 5)
print(" any(t4) -> ", any(t4))


