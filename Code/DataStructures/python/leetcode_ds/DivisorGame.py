class Solution:
    def divisorGame(self, N: int) -> bool:
        return (N % 2 == 0)




s = Solution()
b = s.divisorGame(2)
print('b -> ', b)