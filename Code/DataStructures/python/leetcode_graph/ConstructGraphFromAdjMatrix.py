from typing import List
from collections import defaultdict

class ConstructGraphFromAdjMatrix:

    def graphFromAdjMatrix_adjList(self, m: List[List[int]]):

        graph = defaultdict(list)

        for k, v in m:
            graph[k].append(v)

        print(graph)

        pass



    def graphFromAdjMatrix_adjMatrix(self, m:List[List[int]]):

        # graph = defaultdict(list)

        graph = [[[] for _ in range(len(m))]]
        # for s, e, w in m:
        #     graph[s].append((e, w))


        print(" graph from AdjMatrix -> ", graph)

        pass




soln = ConstructGraphFromAdjMatrix()
adjList = [[1,2], [2,3], [3,1], [3,4]]
soln.graphFromAdjMatrix_adjList(adjList)

binaryMatrix = [[0, 1, 0, 1, 0],
                [0, 0, 1, 1, 1],
                [1, 0, 0, 1, 0],
                [0, 1, 1, 0, 0],
                [1, 0, 1, 0, 1]
                ]

soln.graphFromAdjMatrix_adjMatrix(binaryMatrix)

