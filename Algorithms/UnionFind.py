# reference - https://www.geeksforgeeks.org/union-find/
# https://www.youtube.com/watch?v=eTaWFhPXPz4
# https://www.youtube.com/watch?v=mFVivXZrwyg
# https://www.geeksforgeeks.org/union-find/
# https://www.youtube.com/watch?v=kaBX2s3pYO4&t=786s

from typing import List
from collections import defaultdict

class UnionFind:

    def __init__(self, numVertices):
        self.numVertices = numVertices
        self.connections = defaultdict(list)
        self.parents=[-1 for _ in range(numVertices)]
        # self.vertices = [range(numVertices+1)]

    def addVertex(self, n1):
        if n1 <= self.numVertices-1:
            self.parents[n1]=-1
        else:
            print(" node > numVertices-1")

    def addEdge(self, n1, n2):
        self.connections[n1].append(n2)
        self.connections[n2].append(n1)
        self.parents[n2]=n1

    # get the root parent
    def find(self, n1):
        if self.parents[n1] == -1:
            return n1

        nextIndex = self.parents[n1]

        return self.find(nextIndex)

    # point parent of v1 to v2
    def union(self, node1, node2):
        toproot = self.find(node1)
        # childroot = self.find(node2)
        self.parents[node2] = toproot

    def isCyclic(self, n1, n2):
        toproot_n1 = self.find(n1)
        toproot_n2 = self.find(n2)
        if toproot_n1 == toproot_n2:
            return True
        else:
            self.addEdge(n1,n2)
            return False



sol = UnionFind(10)
sol.addVertex(0)
sol.addVertex(1)
sol.addVertex(2)
sol.addVertex(3)
sol.addVertex(4)

sol.addVertex(5)
sol.addVertex(6)
sol.addVertex(7)

sol.addEdge(0,1)
sol.addEdge(0,2)
sol.addEdge(2,3)

sol.addEdge(5,6)
sol.addEdge(6,7)

print(" connections -> ", sol.connections)
print(" parents -> ", sol.parents)

res=sol.find(2)
print(" root of 1 -> ", res)

sol.union(1, 4)
print(" after union -> parents -> ", sol.parents)

print(" top most parent of 4 -> ",sol.find(4))
print(" top most parent of 7 -> ",sol.find(7))
print(" top most parent of 5 -> ",sol.find(5))

# sol.union(3,5)
# Graph -> set of vertices and Edges
# print(" after union, top most parent of 7 -> ",sol.find(7))

canCauseCycle=sol.isCyclic(5,7)
print(" joining 5,7 can cause cycle -> ", canCauseCycle)