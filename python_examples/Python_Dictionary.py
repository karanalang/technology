from collections import defaultdict, OrderedDict
from typing import List


class Python_Dictionary:

    def usingDefaultDict(self, l:List):

        dd_defautInt = defaultdict(int)
        for k,v in l:
            dd_defautInt[k] = v

        print(" defaultDict, default int -> ",dd_defautInt)
        print(" trying to get value not present in defaultdict int -> ", dd_defautInt['NA'])

        dd_defaultList = defaultdict(list)
        for k, v in l:
            dd_defaultList[k].append(v)

        print(" defaultDict List -> ", dd_defaultList)
        print(" trying to get value not present in defaultdict list -> ", dd_defaultList['NA'])

        dd_default_lambda_35 = defaultdict(lambda :35)
        for k, v in l:
            dd_default_lambda_35[k] = v

        print(" key present in defaultdict -> ", dd_default_lambda_35[0], ' key not present in dd_default_lambda -> ', dd_default_lambda_35['NA'])

        dd_default_lambda_None = defaultdict(lambda: None)
        for k, v in l:
            dd_default_lambda_None[k] = v

        print(" key present in defaultdict -> ", dd_default_lambda_None[0], ' key not present in dd_default_lambda -> ',
              dd_default_lambda_None['NA'])

        print(" looping through dd_defaultList")

        for k, c in dd_defaultList.items():
            print(" dd_defaultList, k -> ", k, " v -> ", v)

        print(" looping through dd_default_lambda_None")

        for k, c in dd_default_lambda_None.items():
            print(" dd_default_lambda_None, k -> ", k, " v -> ", v)


    def usingPythonDict(self):

        myDict = {'d':1, 'a':2, 'c':3}
        print("Using regular dict, does not provide default value -> ", myDict['a'], " print myDict -> ", myDict)

        myDict2 = dict({'ab':2, 'bc':3, 'de':4})
        print(" myDict2, using dict keyword -> ", myDict2)

        try:
            print(" geting value not present in dict -> ", myDict2['NA'])
        except:
            print(' In Except -> value not available')


        myDict3 = dict([['a',2], ['b', 5], ['a',10]])
        print(" converting List[List[int]] to myDict3 -> ", myDict3)

        myDict4 = dict((['a2',21], ['b1', 51], ['a1',11]))
        print(" converting tuple(arrays) to myDict4 ->  ", myDict4)

        print(" type(arrays) -> ", type((['a2',21], ['b1', 51], ['a1',11])))


    def usingOrderedDict(self, ll):
        ordDict = OrderedDict()

        for k, v in ll:
            ordDict[k] = v

        print(" orderedDict -> ", ordDict)

        OrderedDict.pop()

        print(" orderedDict after pop -> ", ordDict)







sol = Python_Dictionary()
# sol.usingPythonDict()
ll = [[0,1], [2, 5], [2, 4]]
sol.usingDefaultDict(ll)
sol.usingOrderedDict(ll)
