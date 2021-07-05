class PythonSet :

    def checkObjectInSet(self, s:set, i :int):

        print(" s is -> ", s)

        if i in s:
            print(" i present in set -> ", s, " i -> ", i)
            return True
        else:
            print(" i not in set ", s, " i -> ", i)
            return False



    def addToSet(self, s, i):
        s.add(i)
        return s


    def intersetionOfSets(self, s1:set, s2:set):
        i1 =  s1.intersection(s2)
        print(" i1 using intersection -> ", i1)

        i2 = s1 & s2
        print(" i2 using & ", i2)


    def unionSets(self, s1:set, s2:set):
        u1 = s1.union(s2)
        print(" u1 -> ", u1)

        u2 = s1 | s2
        print(" u2 -> ", u2)


    def differenceOfSets(self, s1, s2):

        s1_minus_s2 = s1 - s2
        print(" s1_minus_s2 -> ", s1_minus_s2)

        print(" s2_minus_s1 -> ", (s2 - s1))


    def symetricDifference(self, s1, s2):

        print(" symetricDifference : elements in both sets Except common elements ", (s1^s2))
        # pass

    def setComprehension(self, s1:set):
        a = {x for x in s1 if x not in 'abc'}
        print(" a -> ", a)


l = [2, 4, 6, 7, 9, 2, 1, 1.5]
s = set(l)

ps = PythonSet()
inSet = ps.checkObjectInSet(s, int(1.5))
print(" inSet -> ", inSet)


s1 = ps.addToSet(s, 20)
print(s1)

s1 = {2, 3, 51, 20, 3}
s2 = {5, 3}

ps.intersetionOfSets(s1, s2)
ps.unionSets(s1,s2)

ps.differenceOfSets(s1,s2)
ps.symetricDifference({1, 4, 31}, {4, 31, 30})

A = set('abcdefg')
ps.setComprehension(A)