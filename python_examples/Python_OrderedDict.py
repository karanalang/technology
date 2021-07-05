from collections import OrderedDict

class Python_OrderedDict:

    def usingOrderedDict(self, ll):
        ordDict = OrderedDict()

        for k, v in ll:
            ordDict[k] = v

        print(" orderedDict -> ", ordDict)
        for k, v in ordDict.items():
            print("1. k -> ", k, " v -> ", v)

        ordDict[0] = '000'

        print(" orderedDict after value change, Order is maintained -> ", ordDict)
        for k, v in ordDict.items():
            print(" 2. k -> ", k, " v -> ", v)


        print(" deleting key = 0 from ordDict")
        ordDict.pop(0)

        print(" orderedDict after pop -> ", ordDict)

        ordDict[0] = 'reentered'

        print(" orderedDict after pop & re-add -> ", ordDict)
        for k, v in ordDict.items():
            print(" 3. k -> ", k, " v -> ", v)


sol = Python_OrderedDict()
ll = [[0, 1], [2, 5], [21, 4]]
sol.usingOrderedDict(ll)
