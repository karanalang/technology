from typing import List
import bisect

class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:

        if (len(stones) == 0):
            return 0

        i = 0
        while len(stones) >= 1:

            if(len(stones) == 1):
                return stones[0]

            # stones = stones[0 : len(stones)]
            stones = self.sortStones(stones)
            # print('stones -> ', stones)

            if(stones[i] == stones[i+1]):
                wt = 0
            else:
                if(stones[i] > stones[i+1]):
                    wt = stones[i] - stones[i+1]
                else:
                    wt = stones[i+1] - stones[i]

            # print(' wt -> ', wt)
            stones.append(wt)
            stones = stones[2 : len(stones)]
            # i = i + 2

        # if(len(stones) == 1)
        return wt


    def sortStones(self, stones) -> List[int]:

        sortedStones = sorted(stones, reverse=True)
        return sortedStones


    def lastStoneWeight2(self, stones: List[int]) -> int:

        if(len(stones) == 0):
            return 0
        if(len(stones) == 1):
            return stones[0]

        stones.sort()
        print(' stones after sorting ', stones)
        x = stones.pop()
        y = stones.pop()

        print(' x pop -> ', x, ' y pop ', y)

        if((x - y) != 0):
            bisect.insort(stones, (x-y))
        return self.lastStoneWeight2(stones)




stones = [2,7,4,1,8,1]
s = Solution()
lastStoneWeight = s.lastStoneWeight2(stones)
print(' lastStoneWeight -> ', lastStoneWeight)
