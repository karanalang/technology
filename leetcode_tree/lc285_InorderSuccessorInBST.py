# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """

    def inorderSuccessor(self, root, p):
        # write your code here
        if not root or not p:
            return None

        def findStartNode(root):
            if p.val == root.val:
                return root
            elif p.val > root.val:
                root = root.right
            elif p.val < root.val:
                return root

            return None

        def getInorderSuccessor(nd):
            nd = nd.right
            while nd.left:
                nd = nd.left

            return nd

        startNode = findStartNode(root)
        if startNode:
            return getInorderSuccessor(startNode)


sol = Solution()




