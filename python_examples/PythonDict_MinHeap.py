from collections import defaultdict

class Python_Dict_MinHeap:

    def popFromDefaultDict(self):
        d = defaultdict(int)
        d[1] = 1
        d[2] = 2
        d[3] = 3
        d[4] = 4
        print(d)
        d.pop(1)
        print(d)
        del d[2]
        print(d.items())



sol = Python_Dict_MinHeap()
sol.popFromDefaultDict()
