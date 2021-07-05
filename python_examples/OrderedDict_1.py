from collections import OrderedDict

class OrderedDit_1:

    def __init__(self):
        self.od = OrderedDict()

    def addToOrderedDict(self):

        self.od['A'] = 4
        self.od['B'] = 3
        self.od['C'] = 2
        self.od['D'] = 1

    def changeValueOfKeyOD(self):

        self.od['A'] = 0
        print(" Order of keys is not changed after Value change i.e. it retains the same order -> ", self.od)

    def printOrderedDict(self):

        for item in self.od.items():
            print(" OrderedItem item -> ", item)

        for k, v in self.od.items():
            print("  key -> ", k, " value -> ", v)


    def popFromOrderedDict(self):

        self.od.pop('A')
        print(" od after od.pop() ", self.od)

    def popFromOrderedDict_2(self):

        self.od.popitem()
        print(" od after od.popitem i.e. FIFO ", self.od)

    def popFromOrderedDict_3(self):

        self.od.popitem(last=True)
        print(" od after od.popitem(last=True) ", self.od)

    def popFromOrderedDict_4(self):

        self.od.popitem(last=False)
        print(" od after od.popitem(last=True) ", self.od)

    def reorder_Move_to_End(self,key):

        self.od.move_to_end(key, last=True)
        print(" od after self.od.move_to_end(last=True) ", self.od)
        self.od.move_to_end('D', last=False)
        print(" od after self.od.move_to_end(last=False) ", self.od)

    def getItmeFromOrderedDict(self, key):
        try:
            it = self.od[key]
            print(" item with key -> ", key, "  <- available")
        except:
            print(" except block : Item with key -> ", key, " <- not available")


od = OrderedDit_1()
od.addToOrderedDict()
od.printOrderedDict()
od.changeValueOfKeyOD()
od.popFromOrderedDict()
# od.popFromOrderedDict_4()
# od.popFromOrderedDict_3()
# od.popFromOrderedDict_2()
od.reorder_Move_to_End('B')
od.getItmeFromOrderedDict('B')
od.getItmeFromOrderedDict('A1')

