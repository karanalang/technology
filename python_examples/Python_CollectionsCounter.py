# https://www.journaldev.com/20806/python-counter-python-collections-counter

from collections import Counter

class Python_CollectionsCounter:

    def usingCollectionsCounter(self):

        ctr = Counter()
        print("Item in empty counter -> ", ctr.elements())

        ctrWithInitialValues = Counter(['a', 'a', 'b', 'c', 'c', 'c'])
        print("ctrWithInitialValues -> ",ctrWithInitialValues)

        ctrWithInitialValues2 = Counter(a=2, b=3, c=5)
        print("ctrWithInitialValues2 -> ", ctrWithInitialValues2)


sol = Python_CollectionsCounter()
sol.usingCollectionsCounter()