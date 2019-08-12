from typing import List

class Solution:



    def fib_recursive(self, N: int) -> int:
        if(N == 0):
            return 0

        if(N == 1):
            return 1

        return self.fib_recursive(N-1) + self.fib_recursive(N-2)


    def fib_dynamicProgramming(self, N:int) -> int:

        fibArray = []
        # fibArray.append(0)
        fibArray.append(1)
        fibArray.append(1)

        return self.fib_dp(N, fibArray)


    def fib_dp(self, N:int, fibArray:List) -> int:

        if(N == 0):
            return 0

        print(" 1. ", fibArray, " len(fibArray) -> ", len(fibArray), " N -> ", N)
        if (N == 1 or N ==2):
            print("N ==1 or N ==2, returning 1")
            return 1

        # if(N ==2) :
        #     return 1



        if(N > len(fibArray)):
        # if (N > len(fibArray) -1):
            tempfib = self.fib_dp(N - 1, fibArray) + self.fib_dp(N - 2, fibArray)
            print(" N > len(fibArray), adding to fibArray => ", tempfib, " <- N -> ", N, " <-fibArray -> ", fibArray)
            fibArray.append(tempfib)
            # return tempfib
        else:
            tempfib = fibArray[N-1]
            # tempfib = fibArray[N]
            print(" 3. N lt len(fibArray)..  N ", N, " <- fibArray -> ", fibArray, " <- tempfib -> ", tempfib)
            # return fibArray[N]

        return tempfib

    #
    def fibonacci(self, n):
        """Return the nth Fibonacci number."""
        # r[i] will contain the ith Fibonacci number
        r = [-1] * (n + 1)
        return self.fibonacci_helper(n, r)

    def fibonacci_helper(self, n, r):
        """Return the nth Fibonacci number and store the ith Fibonacci number in
        r[i] for 0 <= i <= n."""
        if r[n] >= 0:
            return r[n]

        if (n == 0 or n == 1):
            q = n
        else:
            q = self.fibonacci_helper(n - 1, r) + self.fibonacci_helper(n - 2, r)
        r[n] = q

        return q



"""
fib(0) = 0
1 = 1
2 = 1
3 = 2
4 = 3
5 = 5
6 = 8

"""


s = Solution()
# fib_no = s.fib_recursive(200)
# print(fib_no)
fib_dp = s.fib_dynamicProgramming(7)
print(" fib_dp -> ", fib_dp)


# fib_dp2 = s.fibonacci(5)
# print(fib_dp2)