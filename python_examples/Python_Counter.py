from collections import Counter

class PythonCounter:

    def usingCounterElements(self, s):
        x = Counter(s)
        print(" x -> ", x)

        for elem in x.elements():
            print(" element in string, using python counter.elements -> ", elem)
        # print(" type(x.elements()) -> ", type(x.elements()))

        for cnt in x.values():
            print(" cnt i.e x.values() -> ", cnt)

        mostCommon = x.most_common(2)
        for m in mostCommon:
            print(" most Common elem -> ", mostCommon)

p = PythonCounter()
s = 'aab'
# p.usingCounterElements(s)
p.usingCounterElements({'a':1, 'b':2, "c":3})
# p.usingCounterElements({'aa':1, 'bb':3, 'cc':6})
# p.usingCounterElements([1, 2, 3, 7, 9, 4, 5])
# p.usingCounterElements([1, 2, 3, 7, 9, 4, 5])

