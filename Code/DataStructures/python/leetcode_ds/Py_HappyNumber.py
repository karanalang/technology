class Solution:

    # def isHappy(self, n: int) -> bool:
    #     sum12 = self.SumOfSquares(n, 0)
    #     print(" sum12 ", sum12)
    #     if(sum12 == 1):
    #         return True
    #     else:
    #         return False
    #
    # def SumOfSquares(self, n:int, sum:int) -> int:
    #
    #     s1 = sum(pow(int(digit),2) for digit in str(n))
    #     while (s1 >= 10):
    #         self.SumOfSquares()
    #
    #     print('s1 -> ', type(s1), s1)
    #     if (s1 >= 10):
    #         self.SumOfSquares(s1)
    #     else:
    #         print(' type(s1) -> ', type(s1), "RETURNing ", s1)
    #         return s1
        # return s1


    def isHappy2(self, n:int) -> bool:
        seen = set([n])
        while n!= 1 :
            print("n != 1 -> ", n)
            n = sum(int(digit) ** 2 for digit in str(n))
            if n in seen:
                return False
            seen.add(n)
        return True



s = Solution()
isHappy = s.isHappy2(19)
print("isHappy -> ", isHappy)
# sumOfSquares = s.SumOfSquares111(101)
# print('sumOfSquares -> ', sumOfSquares)