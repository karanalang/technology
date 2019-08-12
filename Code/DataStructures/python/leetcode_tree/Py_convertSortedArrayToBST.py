from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        t2 = self.createBST(nums, 0, len(nums) -1)
        return t2

    def createBST(self,nums, start, end):

        if(start > end):
            return None

        mid = int((start + end)/2)
        root = TreeNode(nums[mid])

        root.left = self.createBST(nums, start, mid -1)
        root.right = self.createBST(nums, mid +1, end)

        return root


    def createBST_org(self,nums, t1, mid, br_index):

        if(br_index >= 0 and br_index < mid):
            t1.left = TreeNode(nums[br_index])
            self.createBST(nums, t1.left, mid, br_index -1)

        # while(br_index >= 0):
        #     t1.left = TreeNode(nums[br_index])
        #     # t1 = t1.left
        #     br_index -= 1

        if(br_index < 0):
            br_index = mid +1

        # while(br_index < len(nums)):
        #     t1.right = TreeNode(nums[br_index])
        #     # t1 = t1.right
        #     br_index += 1

        if (br_index > mid and br_index < len(nums)):
            t1.right = TreeNode(nums[br_index])
            self.createBST(nums, t1.right, mid, br_index + 1)

        return t1

    def printTree(self, t:TreeNode):

        print(" Tree Node -> ", t.val)
        if(t.left):
            self.printTree(t.left)

        if(t.right):
            self.printTree(t.right)


s = Solution()
n = [1, 2, 3, 4]

t1 = s.sortedArrayToBST(n)
s.printTree(t1)
print(t1.val)

