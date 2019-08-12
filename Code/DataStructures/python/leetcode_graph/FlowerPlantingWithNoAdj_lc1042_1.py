from typing import List
from collections import defaultdict

class FlowerPlantingWithNoAdj:

    def gardenNoAdj(self, N, paths: List[List[int]]) -> List[int]:

        ans = [0 for i in range(N)]

        print(" Number of Gardens is ", N, " ans -> ", ans)

        graph = defaultdict(list)

        for u, v in paths:
            if u < v:
                graph[v - 1].append(u - 1)
            else:
                graph[u - 1].append(v - 1)

        print(" gardenAndNeighbors -> ", graph)

        # flowerTypes = set(range(1,5))
        # print(flowerTypes)

        # for each
        for i in range(N):
            if not graph[i]:
                ans[i] = 1
            else:
                ans[i] = [j for j in range(1, 5) if j not in [ans[l] for l in graph[i]]][0]

        return ans


        # for i in range(N):
        #     for l in graph[i]:
        #         print(" l is -> ", l)


        # for l in range(len(paths)):
        #     print(paths[l][0])


        return res
        # pass



g = FlowerPlantingWithNoAdj()
paths = [[1,2],[2,3],[3,1]]
ans = g.gardenNoAdj(3, paths)
print(" ans -> ", ans)