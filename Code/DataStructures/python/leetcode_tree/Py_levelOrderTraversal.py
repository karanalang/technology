from multiprocessing import Queue as mQueue
from collections import deque
from queue import Queue as qQueue
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    def levelOrderTraversal_iterative(self, root:TreeNode) -> List[List[int]]:

        q = deque()

        if(root):
            print(" root -> ", root.val)
            q.append(root)

        levelOrderList = []

        while(len(q) != 0):

            currList = []

            size_ = len(q)
            for i in range(size_):
                p = q.popleft()
                currList.append(p.val)
                if(p.left):
                    q.append(p.left)
                if(p.right):
                    q.append(p.right)

            levelOrderList.append(currList)

        return levelOrderList


root = TreeNode(3)
l11 = TreeNode(9)
l12 = TreeNode(20)
l21 = TreeNode(15)
l22 = TreeNode(7)

root.left = l11
root.right = l12
l12.left = l21
l12.right = l22


s = Solution()
l = s.levelOrderTraversal_iterative(root)
print(" l -> ", l)
