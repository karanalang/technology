import heapq

class PriorityQueue_HeapQ:

    def priorityQ_minHeap(self, S:str):

        minHeap = [(S.count(x), x) for x in set(S)]
        print(minHeap)

        heapq.heapify(minHeap)
        print(" disct after heapify -> ", minHeap)

        heapq.heappush(minHeap, (0  , 'zzz'))
        print(" heap after heappush -> ", minHeap)

        while minHeap:
            pop1 = heapq.heappop(minHeap)
            print(" pop item -> ", pop1, " min Heap after pop 1st item -> ", minHeap)




    def priorityQ_maxHeap(self, S:str):

        maxHeap = [(-S.count(x), x) for x in set(S)]
        print(maxHeap)

        heapq.heapify(maxHeap)
        print(" disct after heapify -> ", maxHeap)

        heapq.heappush(maxHeap, (-24, 'ddd'))

        while maxHeap:
            pop1 = heapq.heappop(maxHeap)
            print(" pop item -> ", pop1[0]*(-1), " min Heap after pop 1st item -> ", maxHeap)




sol = PriorityQueue_HeapQ()
s1 = "aaabbbcccccccd"
sol.priorityQ_minHeap(s1)

sol.priorityQ_maxHeap(s1)





