class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, c=0) -> ListNode:


        s = l1.val + l2.val + c
        print(" 1.s -> ", s)
        if(s >= 10):
            c = s//10
            s = s%10
        else:
            c = 0


        print(" 1.s -> ", s, " c -> ", c)
        res = ListNode(s)


        # if either l1 or l2 is Null, add a leaf node with val =0
        if (l1.next or l2.next):
            if l1.next is None:
                print(" l1.next is None ")
                l1.next = ListNode(0)
            if l2.next is None:
                print(" l1.next is None ")
                l2.next = ListNode(0)
            res.next = self.addTwoNumbers(l1.next, l2.next, c)
        # both l1 & l2 are none, but c is not None
        elif c != 0:
            res.next = ListNode(1)

        return res


sol = Solution()
l1 = ListNode(2)
l1_1 = ListNode(4)
l1_2 = ListNode(3)

l1.next = l1_1
l1_1.next = l1_2

l2 = ListNode(5)
l2_1 = ListNode(6)
l2_2 = ListNode(4)

l2.next = l2_1
l2_1.next = l2_2

l3 = ListNode(5)
l4 = ListNode(5)


l5 = ListNode(0)
l6 = ListNode(7)
l7 = ListNode(3)
l6.next = l7

# lsum = sol.addTwoNumbers_2(l3, l4)
lsum = sol.addTwoNumbers(l5, l6)
# lsum = sol.addTwoNumbers(l1, l2)
# print(lsum.val)
while (lsum != None):
    print(" lsum -> ", lsum.val)
    lsum = lsum.next

