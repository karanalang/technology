from typing import List

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:

        aSquared = [i*i for i in A]
        print(sorted(aSquared))
        return aSquared.sort()



s = Solution()
a = [-4,-1,0,3,10]
s.sortedSquares(a)
