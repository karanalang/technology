class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:

        if(not root):
            return None

        # if((L <= root.val <= R) and (not root.left and not root.right)):
        #     return root

        if(root.val > R):
            return self.trimBST(root.left, L, R)

        if(root.val < L):
            return self.trimBST(root.right, L, R)

        if(root.val <= R and root.val >= L):
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
            return root







t1 = TreeNode(1)
t2 = TreeNode(0)
t3 = TreeNode(2)

t1.left = t2
t1.right = t3




t1 = TreeNode(1)
t2 = TreeNode(0)
t3 = TreeNode(2)
t1.left = t2
t1.right = t3


s = Solution()
t_trimmed = s.trimBST(t1, 1, 3)