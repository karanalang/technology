from typing import List
from collections import defaultdict

class Solution_1042:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:

        ans = [0 for i in range(N)]
        print(" 1.ans -> ", ans)
        print(" 2.paths -> ", paths)
        graph = defaultdict(list)
        print(" 1.graph -> ", graph)

        for u, v in paths:
            print(" u -> ", u, " v -> ", v)
            if u < v:
                graph[v - 1].append(u - 1)
            else:
                graph[u - 1].append(v - 1)

        print(" 2. graph -> ", graph)

        for i in range(N):
            print(" graph[i] -> ", graph[i], " i -> ", i)
            if not graph[i]:
                ans[i] = 1
                print(" 1. not gragh[i] ->  ans[i] -> ", )
            else:
                ans[i] = [j for j in range(1, 5) if j not in [ans[l] for l in graph[i]]][0]
                print(" 2. else block.. ans[i] -> ", ans[i], " graph[i] -> ", graph[i])

        return ans

    def gardenNoAdj_2(self, N: int, paths: List[List[int]]) -> List[int]:
        res = [0] * N
        gardenGraph = defaultdict(set)
        for gardenPair in paths:
            gardenGraph[gardenPair[0] - 1].add(gardenPair[1] - 1)
            gardenGraph[gardenPair[1] - 1].add(gardenPair[0] - 1)
        paintMatrix = [[True] * 4 for i in range(N)]
        for garden in range(N):
            for color in range(4):
                if paintMatrix[garden][color]:
                    res[garden] = color + 1
                    for gardenNeighbor in gardenGraph[garden]:
                        paintMatrix[gardenNeighbor][color] = False
                    break
        return res



# https://leetcode.com/problems/flower-planting-with-no-adjacent/discuss/290930/Python-Greedy-Concise-%2B-Explanation

        

s= Solution_1042()
N = 3
paths = [[1,2],[2,3],[3,1]]
ans = s.gardenNoAdj(3, paths)
print(" ans -> ", ans)
