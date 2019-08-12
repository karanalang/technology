from typing import List
from functools import lru_cache

class Solution:
    def stoneGame(self, piles:List[int]) -> bool:

        if not piles:
            return False

    #     int = self.play(0, len(piles) -1, piles, sum)
    #
    #
    # def play(self, i, j, piles): # sum = points with Alex - points with lee
    #
    #     if(i > j): return 0
    #
    #     parity = (j -i +1) %2
    #     if(parity == 0): #first player
    #         return max(piles[i] + self.play(i+1, j), piles[j] + self.play(i, j-1))
    #     else:
    #         return min(-piles[i] + )