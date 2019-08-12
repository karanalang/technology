# https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/
# https://stackoverflow.com/questions/5368326/python-dfs-and-bfs

from typing import List
from collections import deque
from collections import defaultdict

class GraphTraversal:


    def recursive(self, graph:dict, start, path=[]):

        if(start not in graph.keys()):
            # return None
            return []

        path = path + [start]

        for node in graph[start]:
            if not node in path:
                path = self.recursive(graph, node, path)

        return path


    def iterative_dfs(self, graph:dict, start, visited=[]):
        # uses a STACK , LIFO

        stack = [start]
        while(stack):
            print(" stack -> ", stack)
            key = stack.pop(0)
            print(" q.pop(0) -> ", key)
            if key not in visited:
            # for i in range(len(graph[key])):
                visited = visited + [key]
                # add to stack in the front
                stack = graph[key] + stack

        return visited


    def iterative_bfs(self, graph:dict, start, visited=[]):
        # BFS - uses a queue - FIFO

        queue = [start]
        while(queue):
            key = queue.pop(0)
            if key not in visited:
                visited = visited + [key]
                # add graph[key] to the back of the queue
                print(" graph[key] ", graph[key])
                queue = queue + graph[key]
                print(" queue -> ", queue)

        return visited



graph = {'A':['B','C'],'B':['D','E'],'C':['D','E'],'D':['E'],'E':['A']}
gt = GraphTraversal()
path = gt.recursive(graph, 'A')
print(" recursive path => ", path)

visited_dfs = gt.iterative_dfs(graph, 'A')
print(" visited_dfs -> ", visited_dfs)

visite_bfs = gt.iterative_bfs(graph, 'A')
print(" visited_bfs -> ", visite_bfs)