import heapq
from typing import List

class PythonHeap:

    def convertListToHeap(self, l:List[int]):

        print(" l before heapify -> ", l)
        heapq.heapify(l)
        print(" list after heapify ", list(l))

    def pushToHeap(self, l, ele:int):

        heapq.heapify(l)
        heapq.heappush(l, ele)
        print(" list after heappush ", list(l))


    def popFromHeap(self, l):

        heapq.heapify(l)
        heapq.heappop(l)
        print(" list after heappop, smallest item is popped ", list(l))


    def poppush_together(self, l, ele):

        print(" list Before heappushppop ", list(l))
        heapq.heapify(l)
        heapq.heappushpop(l, ele)

        print(" list After heappush ", list(l))

    def heapreplace(self, l,ele):
        print(" list Before heapreplace ", list(l), " element to be added -> ", ele)
        heapq.heapify(l)
        heapq.heapreplace(l, ele)

        print(" list After heapreplace, similar to heapq.heappushpop(h, ele) ->  ", list(l))


    def NLargest(self, n, l, fun=None):

        print(" list in NLargest -> ", l, " n largest -> ",n)
        n_largest = heapq.nlargest(n,l)
        print(" n_largest -> ", n_largest)


    def NSmallest(self, n, l, fun=None):
        print(" list in NSmallest -> ", l, " n -> ", n)
        n_smallest = heapq.nsmallest(n, l)
        print(" n_smallest -> ", n_smallest)


    def maxHeap(self, l):

        l1 = [i*(-1) for i in l]
        heapq.heapify(l1)
        for k in l1:
            print(" k -> ", k*(-1))


ph = PythonHeap()
l = [6, 7, 4, 9, 2, 1]
ph.convertListToHeap(l)
ph.pushToHeap(l, 10)
ph.popFromHeap(l)
ph.poppush_together(l, 13)
# ph.heapreplace(l, 23)
#
ph.NLargest(3,l)
# ph.NSmallest(3,l)
#
# ph.maxHeap(l)