from collections import defaultdict

class Py_Graphs:

    def usingGraphs(self, d:defaultdict):
        print(" graph is defaultdict -> ", d)
        print(" keys -> ", type(d.keys()), " d.get(a) -> ", d.get('a'))
        # get the edges
        for key in d.keys():
            print(" graph key -> ", key, "graphs edges -> ", d[key])

        # add a vertex


    def findIsolatedEdges(self, d: defaultdict):

        isolated = []
        for key in d.keys():
            if(not d[key]):
                # print(" Isolated Node -> ", key)
                isolated.append(key)

        for i in isolated:
            print(" Isolated key -> ", i)
        # get all the edges

    def pathBetween2GraphNodes(self):
        return None


    def appendNode(self, s:str, d:defaultdict) -> defaultdict:
        # check if node exists
        if(s not in d.keys()):
            print(s, " not a key in - ", d)
            d[s] = []
            # d.append(s)

        for i in d.keys():
            print(" key in dict -> ", i)

        return d


    # def addEdge(self, e:str, d:defaultdict):



g = Py_Graphs()
d = {'a':['b','c'], 'b':['c','d'], 'c':['d'], 'd':['c'], 'e':['f'], 'f':['c'], 'isolatedNode':[]}
# print(type(d))
# g.usingGraphs(d)
g.findIsolatedEdges(d)

d1 = {'a':['b','c'], 'b':['c','d'], 'c':['d'], 'd':['c'], 'e':['f'], 'f':['c'], 'isolatedNode':[]}

d2 = g.appendNode('newNode', d1)
g.addEdge('e1', d2)

