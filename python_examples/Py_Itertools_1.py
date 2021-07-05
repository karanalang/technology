# https://docs.python.org/3/library/itertools.html
# https://www.geeksforgeeks.org/python-itertools-accumulate/
# https://docs.python.org/3/library/bisect.html
# https://www.tutorialspoint.com/bisect-array-bisection-algorithm-in-python
# https://medium.com/@jasonrigden/a-guide-to-python-itertools-82e5a306cdf8

import itertools
import operator

data = [10, 20, 13, 4, 5]
print(" data -> ", data)
print(" itertool.accumulate -> ", list(itertools.accumulate(data, operator.add)))
print(" itertool.accumulate func=operator.mul -> ", list(itertools.accumulate(data, operator.mul)))

print(" itertool.accumulate func=operator.max -> ", list(itertools.accumulate(data, max)))
print(" itertool.accumulate func=operator.max -> ", list(itertools.accumulate(data, min)))

# print(" INFINITE ITERATORS ")
# res = itertools.repeat(10,3)
# print(" res -> ", res)
# itertools.cycle('ABCD')

print(" COMBINATORIC ITERTOOLS ")
print(" combinations of numbers, size = 2 -> ", list(itertools.combinations([1,2,3],2)))
print(" combinations of numbers, size = 1 -> ", list(itertools.combinations([1,2,3],1)))
print(" combinations of numbers, size = 3 -> ", list(itertools.combinations([1,2,3],3)))
print(" combinations_with_replacement of numbers, size = 2 -> ", list(itertools.combinations_with_replacement([1,2,3],2)))
print(" combinations_with_replacement of numbers, size = 1 -> ", list(itertools.combinations_with_replacement([1,2,3],1)))
print(" combinations_with_replacement of numbers, size = 3 -> ", list(itertools.combinations_with_replacement([1,2,3],3)))
print(" permutations of numbers, size = 2 -> ", list(itertools.permutations([1,2,3],2)))
print(" permutations of numbers, size = 1 -> ", list(itertools.permutations([1,2,3],1)))
print(" permutations of numbers, size = 3 -> ", list(itertools.permutations([1,2,3],3)))

print(" Iterators terminating on the shortest input sequence ")
l = ['A','B','C','D']
# selector = [1 for i in l if i <= 'B' or 0]
selector = [1,0,1,0]
print(" selector -> ", selector)
print(" compress array ", list(itertools.compress(l,selector)))

chain = itertools.chain('ABC', 'DEF', ['pqr'])
print("chain list of iterables , -> ", list(chain))

chain_from_iterable = itertools.chain.from_iterable(['ABC', 'DEF', 'PQR'])
print(" chain_from_iterable -> ", list(chain_from_iterable))

cnt = itertools.count(10,3) # start, step
print(" cnt - is an Iterator -> ", type(cnt))
for i in cnt:
    print(" i -> ", i)
    if i > 15:
        break

cycle = itertools.cycle('ABC')
idx = 0
for c in cycle:
    print(" c -> ", c)
    idx+=1
    if idx == 5:
        break


print(" cartesian product using itertools.product  - similar to 2 for loops ")
product = itertools.product([1,2,3], ['a','b','c'])
for p in product:
    print(" p -> ", p)

it = itertools.repeat(10,3)
for r in it:
    print(" repeat -> ", r)