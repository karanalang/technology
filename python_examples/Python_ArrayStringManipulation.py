class Python_ArrayString:

    def convertToLowerCase(self):
        s = 'Upper'
        print(" string lower -> ", s.lower())

        l = ['a', 'b', 'c']
        ll = [a.lower() for a in l]
        print(" lowercase l -> ", ll)

        l1 = ['A', 'b', 'C']
        lu = [x.upper() for x in l1]
        print(" uppercase l1 -> ", lu)


    def sortString(self, s):

        print(" sorted s, returns a list  ", sorted(s.lower()))
        ss = ''.join(sorted(s.lower()))
        print(" ss -> ", ss)


    def removeDupes(self):

        s = 'Alaska'
        sset = ''.join(sorted(set(s.lower())))
        print(sset)

sol = Python_ArrayString()
# sol.convertToLowerCase()
# sol.sortString('abdeC')
sol.removeDupes()
