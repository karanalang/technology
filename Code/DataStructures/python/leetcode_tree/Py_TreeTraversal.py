from multiprocessing import Queue as mQueue
from collections import deque
from queue import Queue as qQueue
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class TreeTraversal:
    """
        root, left, right

    """
    def preOrder(self, root: TreeNode):

        if (root):
            print(" PreOrderTraversal Node -> ", root.val)
            self.preOrder(root.left)
            self.preOrder(root.right)


    """
    left, root, right
    
    """
    def inOrder(self, root: TreeNode):

        if (root):
            self.preOrder(root.left)
            print(" PreOrderTraversal Node -> ", root.val)
            self.preOrder(root.right)


    def postOrder(self, root: TreeNode):

        if (root):
            self.preOrder(root.left)
            self.preOrder(root.right)
            print(" PreOrderTraversal Node -> ", root.val)


    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        dq = qQueue()
        if(root):
            dq.put(root)

        levelOrderList = []

        while(dq.qsize() != 0):

            size = dq.qsize()
            print('size ', size)
            currList = []
            # pop all items of the list, add to currList
            for i in range(size):
                i = dq.get()
                currList.append(i.val)
                print(" 1. removing from queue -> ", i.val)
                # print(dq.pop())
                # print(i)
                if(i.left):
                    print(" 1.adding to queue -> ", i.left.val)
                    dq.put(i.left)
                if(i.right):
                    print(" 2.adding to queue -> ", i.right.val)
                    dq.put(i.right)
            print(" 1. ", currList)
            levelOrderList.append(currList)

        print(' 2. ', levelOrderList)
        return levelOrderList

    def levelOrder_dq(self, root: TreeNode) -> List[List[int]]:

        dq = deque()
        if (root):
            dq.append(root)

        levelOrderList = []

        while (len(dq) != 0):

            size = len(dq)
            print('size ', size)
            currList = []
            # pop all items of the list, add to currList
            for i in range(size):
                i = dq.popleft()
                currList.append(i.val)
                print(" 1. removing from queue -> ", i.val)
                # print(dq.pop())
                # print(i)
                if (i.left):
                    print(" 1.adding to queue -> ", i.left.val)
                    dq.append(i.left)
                if (i.right):
                    print(" 2.adding to queue -> ", i.right.val)
                    dq.append(i.right)
            print(" 1. ", currList)
            levelOrderList.append(currList)

        print(' 2. ', levelOrderList)
        return levelOrderList

    def spiralOrder(self, root: TreeNode):

        odd_ = deque()
        even_ = deque()
        spriralOrderTraversalList = []

        if (root):
            odd_.append(root)

        while (len(odd_) != 0 or len(even_) != 0):

            print(" odd_ len ", len(odd_), " even len ", len(even_))

            while (len(odd_) != 0):

                currOddList = []

                size_ = len(odd_)
                for i in range(size_):
                    i = odd_.popleft()
                    print(" pop from odd_ ", i.val)
                    currOddList.append(i.val)

                    if (i.left):
                        print(" adding to even -> ", i.left.val)
                        even_.append(i.left)
                    if (i.right):
                        print(" adding to odd -> ", i.right.val)
                        even_.append(i.right)

                print(" 1. adding to spriralOrderTraversalList, currOddList ", currOddList)
                spriralOrderTraversalList.append(currOddList)

                while (len(even_) != 0):

                    currEvenList = []

                    size_ = len(even_)
                    for i in range(size_):
                        i = even_.pop()
                        print(" pop from even List -> ", i.val)
                        currEvenList.append(i.val)

                        if (i.left):
                            odd_.append(i.left)
                        if (i.right):
                            odd_.append(i.right)

                    print(" 2. adding to spriralOrderTraversalList, currEvenList ", currEvenList)
                    spriralOrderTraversalList.append(currEvenList)

            return spriralOrderTraversalList






    def reverseOrder(self, root: TreeNode):
        return None

    def verticalOrder(self, root: TreeNode):
        return None




# t1 = TreeNode(1)
# t2 = TreeNode(3)
# t3 = TreeNode(2)
#
# t1.left = t2
# t1.right = t3

t_traverse = TreeTraversal()

# print(' ----- PRE ORDER ----')
# t_traverse.preOrder(t1)
# print(' ----- IN ORDER ----')
#
# t_traverse.inOrder(t1)
#
#
# print(' ----- POST ORDER ----')
#
# t_traverse.postOrder(t1)


root = TreeNode(3)
l11 = TreeNode(9)
l12 = TreeNode(20)
l21 = TreeNode(15)
l22 = TreeNode(7)

root.left = l11
root.right = l12
l12.left = l21
l12.right = l22


print(' ----- LEVEL ORDER ----')
# t_traverse.levelOrder(root)
t_traverse.levelOrder_dq(root)

