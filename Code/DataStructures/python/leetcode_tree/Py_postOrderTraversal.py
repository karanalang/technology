from TreeNode import TreeNode
from typing import List

class Solution:

    def postOrderTraversal_recursion(self, root: TreeNode) -> List[int]:

        l = []

        if(not root):
            return None

        return self.postOrderTraversal_r(root, l)


    def postOrderTraversal_r(self, root, l):

        if(not root):
            return l

        self.postOrderTraversal_r(root.left, l)
        self.postOrderTraversal_r(root.right, l)
        l.append(root.val)

        return l


    def postOrderTraversal_iterative(self, root):

        print(" <- postOrderTraversal -> ")
        stack = []
        result = []

        while(root or stack):

            while(root):
                stack.append(root)
                root = root.left

            # l = stack.pop()
            # result.append(l)

            if(not root.right):
                p = stack.pop()

            root = l.right

        return None


    def postorderTraversal_leetcode(self, root: TreeNode) -> List[int]:
        ans = []
        if not root:
            return ans
        stack = [(root, False)]
        while stack:
            cur, visited = stack.pop()
            if not cur:
                continue
            if visited:
                ans.append(cur.val)
            else:
                stack.append((cur, True))
                stack.append((cur.right, False))
                stack.append((cur.left, False))
        return ans






root = TreeNode(1)
t1 = TreeNode(2)
t2 = TreeNode(3)
root.left = t1
root.right = t2



s = Solution()
s.postOrderTraversal_iterative(root)
# l_recursion = s.postOrderTraversal_recursion(root)
# print(l_recursion)