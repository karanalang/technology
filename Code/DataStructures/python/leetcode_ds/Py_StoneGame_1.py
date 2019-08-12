from typing import List
from functools import lru_cache

class Solution:
    def stoneGame(self, piles:List[int]) -> bool:

        N = len(piles)

        @lru_cache(maxsize=None)
        def dp(i, j):

            if(i > j):
                return 0

            parity = (j - i +1) %2
            print(" i -> ", i, " - j-> ", j, " parity -> ", parity)
            if(parity == 0):
                print(" 000.. piles -> ", piles)
                print(" parity ==1 -> ", max(piles[i] + dp(i + 1, j), piles[j] + dp(i, j - 1)))
                return max(piles[i] + dp(i+1, j), piles[j] + dp(i, j-1))
            else:
                print(" 111.. piles -> ", piles)
                print(" parity != 0 -> ", min(-piles[i] + dp(i + 1, j), -piles[j] + dp(i, j - 1)))
                return min(-piles[i] + dp(i+1, j), -piles[j] + dp(i, j-1))

        return dp(0, N-1) > 0


    def stoneGame2(self, piles):
        N = len(piles)

        @lru_cache(None)
        def dp(i, j):
            # The value of the game [piles[i], piles[i+1], ..., piles[j]].
            if i > j: return 0
            parity = (j - i - N) % 2
            if parity == 1:  # first player
                print(" 111.. piles is -> ", )
                print(" parity ==1 -> ", max(piles[i] + dp(i + 1, j), piles[j] + dp(i, j - 1)))
                return max(piles[i] + dp(i + 1, j), piles[j] + dp(i, j - 1))
            else:
                print(" parity != 1 -> ", min(-piles[i] + dp(i + 1, j), -piles[j] + dp(i, j - 1)))
                return min(-piles[i] + dp(i + 1, j), -piles[j] + dp(i, j - 1))

        return dp(0, N - 1) > 0

    def stoneGame_working(self, piles):
        return True



    def stoneGame3(self, piles) -> bool:

        sPiles = sorted(piles, reverse=True)

        print("sPiles -> ", sPiles)

        sumA = 0
        sumL = 0

        for i in range(len(sPiles)):
            if(i%2 == 0):
                sumA += sPiles[i]
            else:
                sumL += sPiles[i]

        if(sumA > sumL):
            return True
        else:
            return False

        return True


s = Solution()
l = [3, 7, 2, 2]
l1 = [5,2,20,4,9]
b = s.stoneGame3(l1)
print("b -> ", b)