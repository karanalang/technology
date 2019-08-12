from typing import List
from functools import lru_cache

class Solution:
    def stoneGame_notworking(self, piles: List[int]) -> bool:

        if(len(piles)%2 != 0):
            return False

        if(sum(piles)%2 == 0):
            return False

        print(' piles -> ', piles)
        A = 0
        L = 0
        aPlay = 0
        lPlay = 0

        while piles:
            # assume each player picks the max of the 1st & last items
            if(piles[0] == piles[len(piles)-1]):
                if(lPlay < aPlay):
                    lPlay += 1
                    L += piles[0]
                else:
                    aPlay += 1
                    A += piles[0]
                piles = piles[0:len(piles) - 2]

            if(piles):
                if(piles[0] > piles[len(piles)- 1]):
                    if (lPlay < aPlay):
                        lPlay += 1
                        L += piles[0]
                    else:
                        aPlay += 1
                        A += piles[0]
                    piles = piles[1:len(piles) -1]
                else:
                    if (lPlay < aPlay):
                        lPlay += 1
                        L += piles[len(piles)-1]
                    else:
                        aPlay += 1
                        A += piles[len(piles)-1]
                    piles = piles[0:len(piles)-2]
                    print(piles)

        if(A < L):
            return False
        else:
            return True




s = Solution()
l = [5,3,4,5]
l1 = [8,9,7,6,7,6]
l2 = [9,9,10,1,7,3]
alexWins = s.stoneGame(l2)

print(" alexWins -> ", alexWins)