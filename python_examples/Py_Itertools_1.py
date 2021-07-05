# https://docs.python.org/3/library/itertools.html
# https://www.geeksforgeeks.org/python-itertools-accumulate/
# https://docs.python.org/3/library/bisect.html
# https://www.tutorialspoint.com/bisect-array-bisection-algorithm-in-python

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

chain2str = itertools.chain('ABC', 'DEF')
print("chain2str, -> ", list(chain2str))
for it in chain2str:
    for elem in it:
        print(" elem -> ", elem, " it -> ", it)
