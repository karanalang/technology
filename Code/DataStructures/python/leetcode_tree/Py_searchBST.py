class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:

        if(not root):
            return None

        if(val == root.val):
            return root

        if(val < root.val ): # go left
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)

    def printTree(self, t: TreeNode):
        # print(" PRINTING TREE")
        print(" 1. TreeNode ", t.val)
        if (t.left):
            # print(" 1. Tree Node -> ", t.left.val)
            self.printTree(t.left)

        if (t.right):
            # print(" 2. TreeNode -> ", t.right.val)
            self.printTree(t.right)


s = Solution()

t1 = TreeNode(4)
t1l = TreeNode(2)
t1r = TreeNode(7)
t1ll = TreeNode(1)
t1lr = TreeNode(3)

t1.left = t1l
t1.right = t1r
t1l.left = t1ll
t1l.right = t1lr

t = s.searchBST(t1, 2)
s.printTree(t)