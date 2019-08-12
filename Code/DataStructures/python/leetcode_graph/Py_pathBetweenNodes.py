from typing import List

class GraphNodes:
    def pathBetweenNodes(self, graph:dict, start:str, end:str, l = []) -> List[str]:
        # get the keys
        # for key in  graph.keys():
        #     print(" key -> ", key)

        if(end in l):
            return

        if(start not in graph.keys()):
            return []
        else:
            # key = start
            l.append(start)
            if(end in graph[start]):
                l.append(end)
                return l
            else:
                for node in graph[start]:
                    self.pathBetweenNodes(graph, node, end)

        return l


    def find_path(self, graph:dict, start, end, path=[]):

        path = path + [start]
        if(start == end):
            return path


        if(start not in graph.keys()):
            return None

        for node in graph[start]:
            if node not in path:
                newpath = self.find_path(graph, node, end, path)
                if(newpath):
                    return newpath


        return None


gn = GraphNodes()
graph = {'a':['b','c'], 'b':['c','d'], 'c':['d'], 'd':['c'], 'e':['f'], 'f':['c']}
path = gn.pathBetweenNodes(graph, 'a', 'd')
print(" <- path between nodes -> ", path)

path1= gn.find_path(graph, 'a', 'd')
print(" path1 -> ", path1)
