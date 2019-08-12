from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum_iterative(self, root: TreeNode, sum: int) -> List[List[int]]:
        # pass
        stack = [root]
        paths = []
        tempPathSum = 0
        tempPath = []

        while stack:
            node = stack[-1]
            print(" node val {}".format(node.val))
            tempPathSum += node.val
            tempPath.append(node.val)
            if not node.right and not node.left:
                #leaf node
                # if(tempPathSum == sum):
                paths.append(tempPath)
                tempPath = []
                tempPathSum = 0
            else:
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)

        stack.pop()

        return paths



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
sum = 11
arrOfPaths = sol.pathSum_iterative(root, sum)
print(arrOfPaths)

