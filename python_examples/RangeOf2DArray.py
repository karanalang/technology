from typing import List

class RangeOf2DArray:

    def rangeOf2DArray(self, vertices: int):

        print(vertices)
        # a = [[0 for columns in range(vertices)] for row in range(vertices)]
        graph = [[0 for column in range(vertices)]
                 for row in range(vertices)]
        print(graph)
        # print("pass")


sol = RangeOf2DArray()
vertices = [[1, 2,3, 4],
            [2, 3, 4, 5],
            [3, 4, 5, 6],
            [4, 5, 6, 7]
            ]

sol.rangeOf2DArray(len(vertices))
