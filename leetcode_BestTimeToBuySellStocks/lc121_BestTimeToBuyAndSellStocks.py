from typing import List
import sys

class lc121_BestTimeToBuyAndSellStocks:

    def maxProfit_brute(self, prices: List[int]) -> int:

        maxProfit = 0

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                maxProfit = max(maxProfit, prices[j]-prices[i])

        return maxProfit

    def maxProfit_op1(self, prices: List[int]) -> int:

        if not prices:
            return 0

        maxProfit = 0
        maxSP = prices[-1]

        for i in range(len(prices)-2, -1, -1):
            maxProfit = max(maxProfit, maxSP-prices[i])
            maxSP = max(maxSP, prices[i])

        return maxProfit

    def maxProfit_op2(self, prices: List[int]) -> int:

        maxProfit = 0
        lowestSeen = sys.maxsize

        for i in range(len(prices)):
            maxProfit = max(maxProfit, prices[i] - lowestSeen)
            lowestSeen = min(lowestSeen, prices[i])

        return maxProfit

sol = lc121_BestTimeToBuyAndSellStocks()
prices = [7,1,5,3,6,4]
prices1 = [7, 6, 5, 4, 3, 2,1]
maxP = sol.maxProfit_op1(prices)
print(" maxProfit -> ", maxP)

maxP_1 = sol.maxProfit_op2(prices)
print(" maxProfit -> ", maxP_1)