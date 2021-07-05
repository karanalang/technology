from typing import List
import heapq

class HeapQueue:

    def heapifyList(self, l: List):

        #transform list into heap in constant time
        heapifyList = heapq.heapify(l)
        # print(heapifyList)
        for i in heapifyList:
            print(i)


    def heapifyDict(self, d:dict):

        heapfyDict = heapq.heapify(d)


hq = HeapQueue()
hq.heapifyList([1, 7, 9, 4])

