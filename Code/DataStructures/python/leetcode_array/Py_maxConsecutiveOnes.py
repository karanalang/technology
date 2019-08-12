from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        if(len(nums) == 0):
            return 0

        if(1 not in nums):
            return 0

        if(0 not in nums):
            return len(nums)

        maxCnt = 0
        tempMaxCnt = 0
        len_ = len(nums)
        for i in range(len_):
            if(nums[i] == 0):
                maxCnt = max(tempMaxCnt, maxCnt)
                tempMaxCnt = 0
            else:
                if (nums[i] == 1):
                    tempMaxCnt += 1


        maxCnt = max(tempMaxCnt, maxCnt)
        return maxCnt


    # sliding window
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        maxCnt = 0
        window_start = 0
        for window_end in range(len(nums)):
            if(nums[window_end] == 1):
                maxCnt = max(maxCnt, window_end - window_start + 1)
            else:
                window_start = window_end + 1


        return maxCnt



s = Solution()
l = [1,1,0,1,1,1]
maxCnt = s.findMaxConsecutiveOnes(l)
print(maxCnt)
