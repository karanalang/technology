class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        if(not root):
            return 0

        if(not root.left and not root.right):
            return 1

        return self.checkDepth(root, 0)


    def checkDepth(self, root, maxDepth) -> int:

        if(not root):
            return maxDepth

        if(root):
            maxDepth += 1

        if(not root.left and not root.right):
            return maxDepth

        return max(self.checkDepth(root.left, maxDepth), self.checkDepth(root.right, maxDepth))


t1 = TreeNode(3)
t2 = TreeNode(9)
t3 = TreeNode(20)
t4 = TreeNode(15)
t5 = TreeNode(7)

t1.left = t2
t1.right = t3
t3.left = t4
t3.right = t5

s = Solution()
dep = s.maxDepth(t1)
print(" maxDepth -> ", dep)
