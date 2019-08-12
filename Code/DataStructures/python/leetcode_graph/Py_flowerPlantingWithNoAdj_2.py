from typing import List

class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:

        ans = [0] * N
        flowers = [1, 2, 3, 4]
        fIndex = -1

        for i in range(0, N):
            fIndex = fIndex +1
            ans[i] = flowers[fIndex]
            ans[i+1] = flowers[fIndex+1]

            if(fIndex == 3):
                fIndex = -1


        return None








N_1 = 3
paths_1 = [[1,2],[2,3],[3,1]]

N_2 = 4
paths_2 = [[1,2], [3,4]]

N_3 = 4
paths_3 = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]


sol = Solution()
sol.gardenNoAdj(N_1, paths_1)
