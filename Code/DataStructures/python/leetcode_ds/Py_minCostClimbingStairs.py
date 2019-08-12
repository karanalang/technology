from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 1],cost[i - 2])
            print(' cost[i] -> ', cost[i])

        print(' cost after -> ', cost)
        return min(cost[-1], cost[-2])


    def minCostClimbingStairs2(self, cost:[List[int]]) -> int:
        # using dynamic programming - bottomup approach
        len_ = len(cost)
        dp = [0] * len_
        # min cost to reach the 0th floor = cost[0]
        dp[0] = cost[0]
        # min cost to reach the 1st floor = cost[1]
        dp[1] = cost[1]
        for i in range(2, len_):
            # min cost to reach the ith floor = min(cost[i] + dp[i-2], cost[i] + dp[i-1],
            # since we can take 1 or 2 steps to
            dp[i] = min(dp[i-2] + cost[i], dp[i-1] + cost[i])

        print('dp -> ' , dp)
        return min(dp[len_-2], dp[len_-1])


s = Solution()
# l = [10, 15, 20]
l = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
minCost2 = s.minCostClimbingStairs2(l)
print('minCost2 -> ', minCost2)

minCost = s.minCostClimbingStairs(l)
print('minCost -> ', minCost)




