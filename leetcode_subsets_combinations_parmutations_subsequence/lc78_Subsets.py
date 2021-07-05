# https://www.youtube.com/watch?v=MsHFNGltIxw
# https://www.youtube.com/watch?v=bGC2fNALbNU
# This structure might apply to many other backtracking questions,
# but here I am just going to demonstrate Subsets, Permutations, and Combination Sum.


from typing import List

class lc78_Subsets:


    # Add path to res at every level
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        return self.dfs(nums, 0, [], res)
        # return res

    def dfs(self, nums, start, path, res):
        res.append(path)
        for i in range(start, len(nums)):
            self.dfs(nums, i+1, path + [nums[i]], res)

        return res


sol = lc78_Subsets()
nums = [1, 2, 3]
res = sol.subsets(nums)
print(" res -> ", res)