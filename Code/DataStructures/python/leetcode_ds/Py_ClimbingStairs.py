class Solution:

    def climbStairs(self, n: int) -> int:
        print("In climb stairs")

        dp = [0] * (n + 1)
        print(" dp initialized -> ", dp)
        dp[0] = 1
        dp[1] = 1

        # since
        for i in range(2, len(dp)):
            print(" i is -> ", i)
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]


    def climbStairs2(self, n: int) -> int:
        print("In climb stairs")

        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1

        print(" dp initialized -> ", dp)
        dplen = len(dp)

        # since
        for i in range(2, len(dp)):
            print(" i is -> ", i)
            dp[i] = dp[i-1] + dp[i-2]
            print(dp[i])


        return dp[n]






s = Solution()
n = 5
num_ways = s.climbStairs2(n)
print('num_ways -> ', num_ways)




# if __name__ == "__main__":
#     s.climbStairs(n=10)