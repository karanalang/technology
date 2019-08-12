from typing import List

class PathBetweenNodes:

    def getAllPathsBetweenNodes(self, graph:dict,start:str,end:str,path=[]):

        # print("start", start)
        path = path + [start]
        # print(" path -> ")


        if (start == end):
            return [path]

        # for key in graph.keys():
        #     print(key)

        if start not in graph.keys():
            return []

        paths=[]
        print(" paths -> ", paths)

        for node in graph[start]:
            if(node not in path):
                newPaths = self.getAllPathsBetweenNodes(graph, node, end, path)
                print(" newPaths -> ", newPaths)
                for newPath in newPaths:
                    paths.append(newPath)

        return paths


    def find_all_paths(self, graph:dict, start, end, path=[]) -> List[List[int]]:
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph.keys():
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = self.find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths


    def maxPathSize(self, paths):

        print(" paths -> ", paths)
        sortedPaths = sorted(paths, key=len, reverse=True)
        print(" sortedPaths -> ", sortedPaths)
        maxPath = sortedPaths[0]
        print(maxPath)
        return len(maxPath)


    def minPathSize(self, paths):

        print(" paths -> ", paths)
        sortedPaths = sorted(paths, key=len)
        print(" sortedPaths -> ", sortedPaths)
        minPath = sortedPaths[0]
        print(minPath)
        return len(minPath)


gn = PathBetweenNodes()
graph = {'a':['b','c'], 'b':['c','d'], 'c':['d'], 'd':['c'], 'e':['f'], 'f':['c']}
allpaths = gn.getAllPathsBetweenNodes(graph, 'a', 'd')
print(" <- All paths -> ", allpaths)

# maxPathSize = gn.maxPathSize(allpaths)
# print(" maxPathSize -> ", maxPathSize)
#
# minPathSize = gn.minPathSize(allpaths)
# print(" minPathSize -> ", minPathSize)
