# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers_1(self, l1: ListNode, l2: ListNode) -> ListNode:

        rem = 0
        s = 0
        res = None

        if(l1 != None and l2 != None):
            s = l1.val + l2.val + rem
            if (s >= 10):
                rem = s / 10
                s = s % 10
            res = ListNode(s)
                # res.next =

        if(l1.next != None and l2.next != None):
            self.joinNodes(l1.next, l2.next, rem, res)

        return res


    def joinNodes(self, l1:ListNode, l2:ListNode, rem, parent:ListNode):

         while(l1 != None and l2 != None):
            s = l1.val + l2.val + rem
            print(" 0.s ", s)
            if (s >= 10):
                rem = int(s / 10)
                s = s % 10
                print("1.s -> ", s)
                print("1. rem -> ", rem)
            print(" 2.rem -> ", rem, " s -> ", s)
            parent.next = ListNode(s)

            l1 = l1.next
            l2 = l2.next
            parent = parent.next
            self.joinNodes(l1, l2, rem, parent)

         # if(l1 and not l2):
         if (l1 != None and l2 == None):
             parent.next = l1

         if(l1 == None and l2 != None):
             parent.next = l2



    def addTwoNumbers(self, l1, l2, c=0):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val = l1.val + l2.val + c
        c = val // 10
        ret = ListNode(val % 10)

        if (l1.next != None or l2.next != None or c != 0):
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            ret.next = self.addTwoNumbers(l1.next, l2.next, c)
        return ret

    def addTwoNumbers_2(self, l1, l2, c=0):

        # add the 2 digits and the carry(c)
        val = l1.val + l2.val + c

        # update the carry
        if val >= 10:
            val = val - 10
            c = 1
        else:
            c = 0

        # // create a new node with the sum
        res = ListNode(val)

        # // if there are still digits in any of the linked lists, keep recurring
        # // if one of the lists is done, create a dummy node with value 0 and keep recurring
        if l1.next or l2.next:
            if l1.next is None:
                l1.next = ListNode(0)

            elif l2.next is None:
                l2.next = ListNode(0)

            res.next = self.addTwoNumbers(l1.next, l2.next, c)
        # if both lists are done, but c is not zero, create another node for c
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


# lsum = sol.addTwoNumbers_2(l3, l4)
lsum = sol.addTwoNumbers_2(l1, l2)
# print(lsum.val)
while(lsum != None):
    print(" lsum -> " , lsum.val)
    lsum = lsum.next

