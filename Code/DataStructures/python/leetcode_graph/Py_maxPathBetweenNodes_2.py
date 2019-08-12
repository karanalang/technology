from collections import deque

class Maxpath_2:

    def find_shortest_path(self, graph, start, end, path=[]):
        path = path + [start]
        if(start == end):
            return path

        if start not in graph.keys():
            return []

        shortest = None

        for node in graph[start]:
            if node not in path:
                newpath = self.find_shortest_path(graph, node, end, path)
                if(newpath):
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath

        return shortest


    def find_shortest_path_bfs(self, graph, start, end):
        dist = {start:[start]}

        q = deque(start)
        while(len(q)):
            at = q.popleft()
            for next in graph[at]:
                if next not in dist:
                    dist[next] = [dist[at], next]
                    q.append(next)

        return dist[end]



mp = Maxpath_2()
graph = {'a':['b','c'], 'b':['c','d'], 'c':['d'], 'd':['c'], 'e':['f'], 'f':['c']}

shortest = mp.find_shortest_path(graph, 'a', 'd')
print(shortest)

shortest_bfs = mp.find_shortest_path_bfs(graph, 'a', 'd')
print(" shortest_bfs -> ", shortest_bfs)