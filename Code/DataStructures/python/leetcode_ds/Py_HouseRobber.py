from typing import List

class Solution:
    def rob1(self, nums: List[int]) -> int:

        l1 = []
        l2 = []

        for i in range(0, len(nums), 2):
            l1.append(nums[i])


        for j in range(1, len(nums), 2):
            l2.append(nums[j])

        s1 =0; s2=0;
        for i in l1:
            s1 += i

        for i in l2:
            s2 += i

        return max(s1,s2)


    # using botton-up approach
    def rob(self, nums:List[int]) -> int:
        if (not nums | len(nums) == 0):
            return 0
        if(len(nums) == 1):
            return nums[0]
        if(len(nums) == 2):
            return max(nums[0], nums[1])

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max((nums[i] + dp[i-2]), dp[i-1])

        # max amount for n houses
        print('dp is -> ', dp)
        return dp[len(nums) -1]





l = [2,7,9,3,1]
s = Solution()
maxRobbed = s.rob(l)
print("maxRobbed -> ", maxRobbed)