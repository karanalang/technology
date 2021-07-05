from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # path = []
        res = []

        def rec(nums, path):
            print(" path is -> ", path, " nums -> ", nums)

            res.append(path)

            for i in range(len(nums)):
                print(" path + nums[i] -> ", path, " nums[i] -> ", nums[i], " path + nums[i] -> ", (path + [nums[i]]))
                rec(nums[i + 1:], path + [nums[i]])

            return res

        return rec(nums, [])


sol = Solution()
nums = [1,2,3]
res = sol.subsets(nums)
print(" res -> ", res)