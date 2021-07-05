# https://data-flair.training/blogs/python-ordereddict/
# https://pymotw.com/3/collections/ordereddict.html
# https://pymotw.com/2/collections/ordereddict.html

from collections import OrderedDict
 # from collections

class UseOrderedDict:

    def __init__(self):
        self.orderedDict = OrderedDict()
        self.regDict = dict()

    def AddToHashMapWithOrder(self, key, val):

        self.orderedDict[key] = val

    def AddToHashMap(self, key, val):
        self.regDict[key] = val


    def printHashMapsContent(self):

        print(" regular Hashmap -> ", self.regDict)
        print(" Ordered Hashmap -> ", self.orderedDict)
        for k, v in self.regDict.items():
            print(" reg hashmap -> key ", k, " val -> ", v)

        for k, v in self.orderedDict.items():
            print(" ordered hashmap -> key ", k, " val -> ", v)

    def compareDicts(self):

        d1 = {}
        d1['b'] = 'B'
        d1['a'] = 'A'

        d2 = {}
        d2['a'] = 'A'
        d2['b'] = 'B'

        print(" comparing 2 hashmaps (Does Not Remember order in which items were added) -> ", (d1 == d2))

    def compareOrderedDicts(self):

        od1 = OrderedDict()
        od1['a'] = 'A'
        od1['b'] = 'B'

        od2 = OrderedDict()
        od2['b'] = 'B'
        od2['a'] = 'A'

        print(" comparing OrderedDicts (remembers order in which items were added) -> ", (od1 == od2))


    def moveItemToEnd_OrderedDict(self):

        od1 = OrderedDict()
        od1['a'] = 'A'
        od1['b'] = 'B'
        od1['c'] = 'C'
        od1['d'] = 'D'

        print(" before moving item ")
        for k, v in od1.items():
            print(" k -> ", k, " v -> ", v)


        od1.move_to_end('b', last=True)
        print(" before moving item, last=True ")
        for k, v in od1.items():
            print(" k -> ", k, " v -> ", v)

        print(" before moving item, last=False ")
        od1.move_to_end('b', last=False)
        for k, v in od1.items():
            print(" k -> ", k, " v -> ", v)


    def deleteItemFromHashMap(self):

        od3 = OrderedDict()
        od3['a'] = 'A'
        od3['b'] = 'B'
        od3['c'] = 'C'
        od3['d'] = 'D'
        od3['e'] = 'E'
        od3['f'] = 'F'
        od3['g'] = 'G'


        print(" before removing item ")
        for k, v in od3.items():
            print(" k -> ", k, " v -> ", v)

        print(" after removing item ")
        del od3['a']
        for k, v in od3.items():
            print(" k -> ", k, " v -> ", v)

        print(" od3.pop ")
        od3.pop('d')
        for k, v in od3.items():
            print(" k -> ", k, " v -> ", v)

        print(" od3.popitem, last = True ")
        od3.popitem(last=True)
        for k, v in od3.items():
            print(" k -> ", k, " v -> ", v)

        print(" od3.popitem, last = False ")
        od3.popitem(last=False)
        for k, v in od3.items():
            print(" k -> ", k, " v -> ", v)





        d3 = {}
        d3['a'] = 'A1'
        d3['b'] = 'B1'
        d3['c'] = 'C1'
        d3['d'] = 'D1'

        print(" before removing item ")
        for k, v in d3.items():
            print(" k -> ", k, " v -> ", v)

        print(" after removing item ")
        del d3['b']
        for k, v in d3.items():
            print(" k -> ", k, " v -> ", v)




od = UseOrderedDict()
od.AddToHashMapWithOrder('a', 'A')
od.AddToHashMapWithOrder('c', 'C')
od.AddToHashMapWithOrder('d', 'D')
od.AddToHashMapWithOrder('e', 'E')
od.AddToHashMapWithOrder('b', 'B')

od.AddToHashMap('a', 'A')
od.AddToHashMap('c', 'C')
od.AddToHashMap('d', 'D')
od.AddToHashMap('e', 'E')
od.AddToHashMap('b', 'B')

od.printHashMapsContent()

od.compareDicts()
od.compareOrderedDicts()

od.moveItemToEnd_OrderedDict()

od.deleteItemFromHashMap()

