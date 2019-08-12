class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:

        if(not t1 and not t2):
            return None

        if(not t1):
            return t2

        if(not t2):
            return t1

        # print("BOTH NODES FOUND, ", t1.val, " t2.val ", t2.val)
        currNode = TreeNode(t1.val + t2.val)
        # print(" MERGED ", t1.val)
        currNode.left = self.mergeTrees(t1.left, t2.left)
        currNode.right = self.mergeTrees(t1.right, t2.right)

        return currNode


    def printTree(self, t:TreeNode):

        # print(" PRINTING TREE")
        print(" 1. TreeNode ", t.val)
        if(t.left):
            # print(" 1. Tree Node -> ", t.left.val)
            self.printTree(t.left)

        if(t.right):
            # print(" 2. TreeNode -> ", t.right.val)
            self.printTree(t.right)


s = Solution()
# t1 = [1,3,2,5]
# t2 = [2,1,3,None,4,None,7]

t1 = TreeNode(1)
t11 = TreeNode(3)
t12 = TreeNode(2)
t13 = TreeNode(5)
t1.left = t11
t1.right = t12
t11.left = t13

t2 = TreeNode(2)
t21 = TreeNode(1)
t22 = TreeNode(3)
t23 = TreeNode(4)
t24 = TreeNode(7)
t2.left = t21
t2.right = t22
t21.right = t23
t22.right = t24

# tm = s.mergeTrees(None, None)
tm = s.mergeTrees(t1, t2)
s.printTree(tm)

print(tm)
