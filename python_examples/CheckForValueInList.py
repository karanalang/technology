# https://www.geeksforgeeks.org/python-ways-to-check-if-element-exists-in-list/
from bisect import bisect_left

class PythonCheckForValueInList:

    def checkForValue(self,l, val):
        print(" val in l - option 1 -> ", (val in l))
        print(" brute force ")
        for v in l:
            if v == val:
                print(" brute, found val ", v)

        print(" using set() +in")
        s = set(l)
        print(" s -> ", s)
        print(" present in set -> ", (val in s))

        print(" using sort() + bisect_left() ")
        l.sort()
        for i in l:
            print(" val after l.sort -> ", i)



sol = PythonCheckForValueInList()
l = [2, 3, 4, 0, 0]
val =0
sol.checkForValue(l, val)