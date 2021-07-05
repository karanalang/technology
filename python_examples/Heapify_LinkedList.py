import heapq
from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Heapify_LinkedList:

    def heapify_LinkedList(self, lists:List[ListNode]):

        res = []
        heapq.heapify(res)
        for l in lists:
            heapq.heappush(res,(l.val))

        ret = ListNode(heapq.heappop())
        currNode = ret
        while len(res) > 0:
            nxt = heapq.heappop(res)
            currNode.next = nxt
            currNode = nxt

        return ret


        # print(res)



        # pass



sol = Heapify_LinkedList()
root = ListNode(0)
n1 = ListNode(1)
n2 = ListNode(2)
root.next = n1
n1.next = n2

root1 = ListNode(6)
n11 = ListNode(7)
n21 = ListNode(8)
root1.next = n11
n11.next = n21



sol.heapify_LinkedList([root, root1])
