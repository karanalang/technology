from typing import List

class NumArray:


    def __init__(self, nums: List[int]):
        # self.num1 = nums
        print(" nums -> ", nums)
        self.dp = [0 for _ in range(len(nums) + 1)]
        print(" <- dp -> ", self.dp)
        for i in range(1, len(nums)+1):
            self.dp[i] = self.dp[i-1] + nums[i-1]
        print(" <- dp 11 -> ", self.dp)


    def sumRange(self, i: int, j: int) -> int:
        sum = 0
        for a in range(i, j+1):
            sum = sum + self.num1[a]

        return sum

    def sumRange1(self, i: int, j: int) -> int:
        l = self.num1[i:j + 1]
        return sum(l)


    def sumRange_dp(self, i:int, j:int):
        return self.dp[j+1] - self.dp[i];


nums = [-2, 0, 3, -5, 2, -1]

obj = NumArray(nums)
# print(obj.sumRange1(0,1))
print(obj.sumRange_dp(0,1))

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)