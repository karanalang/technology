# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:


        if(not root):
            return True
        else:
            val = root.val

        return self.checkUnival(root, val)


    def checkUnival(self, root, val):

        if(not root):
            return True

        if(root.val != val):
            return False

        return (self.checkUnival(root.left, val) and  self.checkUnival(root.right, val))


t1 = TreeNode(2)
t2 = TreeNode(2)
t3 = TreeNode(2)
t4 = TreeNode(5)
t5 = TreeNode(2)

t1.left = t2
t1.right = t3
t2.left = t4
t2.right = t5

s = Solution()
b = s.isUnivalTree(t1)
print("b -> ", b)


