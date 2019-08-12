from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:



        pass



sol = Solution()
# path = [5,4,8,11,null,13,4,7,2,null,null,5,1]
root = TreeNode(1)
node1 = TreeNode(3)
node2 = TreeNode(5)
node3 = TreeNode(4)
node4 = TreeNode(6)
root.left = node1
root.right = node3
node1.left = node2
node3.left = node4