from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def rec(i, tmpArr):

            if i == len(nums):
                res.append(tmpArr)
                return

            print(" i -> ", i, " tmpArr -> ", tmpArr, " res -> ", res)

            currTmpArr = [i for i in tmpArr]
            tmpArr.append(nums[i])

            rec(i + 1, tmpArr)
            rec(i + 1, currTmpArr)

        rec(0, [])
        return res


sol = Solution()
nums = [1,2, 3]
res = sol.subsets(nums)
print(" res -> ", res)
