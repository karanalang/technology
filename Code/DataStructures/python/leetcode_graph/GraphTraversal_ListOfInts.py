from typing import List

class GraphTraversal2:

    def iterative_dfs(self, graph:List[List[int]], start, visited=[]):

        # visited = [start]
        print(" visited -> ", visited)
        stack = [start]
        while(stack):
            key = stack.pop(0)
            print(" key ->", key)
            if key not in visited:
                visited = visited + [key]
                # stack =


        return None



gt2 = GraphTraversal2()
graph = [[1,2], [2, 3], [3,1]]
gt2.iterative_dfs(graph, 1)