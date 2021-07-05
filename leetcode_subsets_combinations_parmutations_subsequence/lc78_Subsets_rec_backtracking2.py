from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def rec(nums, path):
            # print(" path is -> ", path, " nums -> ", nums)

            res.append(path)

            for i in range(len(nums)):
                rec(nums[i+1:], path + [nums[i]])

            # return res

        rec(nums, [])
        return res


sol = Solution()
nums = [1,2,3]
res = sol.subsets(nums)
print(" res -> ", res)