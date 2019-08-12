from collections import defaultdict
from typing import List

# https://www.python.org/doc/essays/graphs/
# https://www.python-course.eu/graphs_python.php

class Py_GraphShortestDistance:

    def distanceBetweenNodes(self, start:str, end:str, graph:defaultdict):

        print(" start -> ", start, " end -> ", end, " graph -> ", graph)

        for k in graph.keys():
            if(k == start):
                print(graph[k])
                if(end in graph[k]):
                    print(" end is availale -> ", end, " key -> ", k)

        return None


    def find_path(self, graph, start, end, path=[]):
        # return None
        path = path + [start]
        print(" path ", path)
        if(start == end):
            return path

        if(start not in graph.keys()):
            print(" start not a key in the graph, returning None")
            return None

        for node in graph[start]:
            # if(not node in path):
                # add to the path
            newpath = self.find_path(graph, node, end, path)
            # if(newpath):
            return newpath

        return None


    def find_all_paths(self, graph, start, end, path=[]):
        return None


    def find_shortest_path(self, graph, start, end, path=[]):
        return None








p = Py_GraphShortestDistance()
graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}

# p.distanceBetweenNodes('A', 'B', graph)


graph1 = ['A', 'B', 'C', 'D']
path = p.find_path(graph, 'A', 'D')
print(" path1 -> ", path)