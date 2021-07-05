from collections import defaultdict

class UsingDefaultDict:

    def addToDefaultDict(self):

        dd_str = defaultdict(str)
        dd_str['a'] = 1
        dd_str[1] = '1'
        print(" defaultdict(str) -> ", dd_str)

        dd_int = defaultdict(int)
        dd_int[1] = '1'
        dd_int[2] = '2'
        dd_int['3'] = 3
        print("dd_int -> ", dd_int)

sol = UsingDefaultDict()
sol.addToDefaultDict()
