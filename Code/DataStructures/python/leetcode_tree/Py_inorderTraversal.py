from typing import List
from TreeNode import TreeNode


class Solution:

    def inorderTraversal_recursive(self, root: TreeNode) -> List[int]:
        results = []
        self.traverse(root, results)
        return results

    def traverse(self, root, results):
        if root is None:
            return
        self.traverse(root.left, results)
        results.append(root.val)
        self.traverse(root.right, results)

    def inorderTraversal_iterative_leetcode(self, root: TreeNode) -> List[int]:
        results, stack = [], []
        cur = root
        while cur or stack:  # KEY: current node not none "or" stack is not empty
            while cur is not None:
                stack.append(cur)
                print(" 1.cur.val ", cur.val)
                cur = cur.left  # check to the leftmost leaf
                if(cur):
                    print(" 2.left leaf ", cur.val)
                else:
                    print(" cur.left is None")
            node = stack.pop()
            print(" 3.node -> ", node.val)
            results.append(node.val)
            cur = node.right  # check if any right leaf

        return results


    def inorderTraversal_iterative(self, root:TreeNode) -> List[int]:
        result = []
        stack = []

        if(root):
            print(" 1.adding to stack ", root.val)
            curr = root

        while(curr or stack):

            while(curr):
                print(" 2. added to stack ", root.val)
                stack.append(curr)
                curr = curr.left

            i = stack.pop()
            result.append(i.val)
            print(" 1. added to result i.val -> ", i.val)

            curr = i.right

        return result

    def inorderTraversal_iterative_1(self, root: TreeNode) -> List[int]:
        result = []
        stack = []

        # if (root):
        #     print(" 1.adding to stack ", root.val)
        #     curr = root

        while (root or stack):

            while (root):
                print(" 2. added to stack ", root.val)
                stack.append(root)
                root = root.left

            i = stack.pop()
            result.append(i.val)
            print(" 1. added to result i.val -> ", i.val)

            root = i.right

        return result


root = TreeNode(1)
t1 = TreeNode(2)
t2 = TreeNode(3)
# t3 = TreeNode(4)
# t4 = TreeNode(5)

root.left = t1
root.right = t2

s = Solution()
# res = s.inorderTraversal_iterative_leetcode(root)
# print(" res -> ", res)

res1 = s.inorderTraversal_iterative_1(root)
print(res1)


