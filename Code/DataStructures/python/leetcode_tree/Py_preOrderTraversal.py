from typing import List
from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def preorderTraversal_recursion(self, root: TreeNode) -> List[int]:

        l = []
        p = deque()
        return self.preOrder(root, l)


    def preOrder(self, root, l:List):

        if(root):
            print(" adding to List -> ", root.val)
            l.append(root.val)
            print(" calling with root.left ", root.left)
            self.preOrder(root.left, l)
            print(" calling with root.right ", root.right)
            self.preOrder(root.right, l)
        else:
            print(" root is Null")

        print("l -> ", l)
        return l

    def preOrderTraversal_iterative(self, root):

        stack = []
        res = []
        if(not root):
            return res
        stack = [root]

        while(stack):
            i = stack.pop()
            res.append(i.val)
            print(" added to res -> ", i.val)

            if (i.right):
                stack.append(i.right)
            if(i.left):
                stack.append(i.left)

            for i in range(len(res)):
                print(" items in res -> ", res[i])

        print(" preOrder2 -> ", res)
        return res








# root = TreeNode(1)
# t1 = TreeNode(2)
# t2 = TreeNode(3)
# root.right = t1
# t1.left = t2


root = TreeNode(1)
t1 = TreeNode(2)
t2 = TreeNode(3)
root.left = t1
root.right = t2

# [3,1,2]


s = Solution()
res = s.preOrderTraversal_iterative(root)
# s.preOrder2(root)
