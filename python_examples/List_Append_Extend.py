class ListExtend:

    def listExtend(self, l, l1):

        print(" list Extend .. input .. l -> ", l, " l1 -> ", l1)
        l.extend(l1)
        print(" list.extend -> ", l)


    def listAppend(self, l, l1):
        print(" list Append ..input ..  l -> ", l, " l1 -> ", l1)
        l.append(l1)
        print(" l.append -> ", l)


    def addItemToEachItemInList(self, l, k):

        print(" l -> ", l, " - k -> ", k)
        # for i in l:
        #     print(" i -> ", i)
        afterAdd = [k+i for i in l]
        print(afterAdd)




s = ListExtend()
l = [1, 2, 3, 4]
l1 = [5, 6]

# print(l.append(l1), l)

s.listExtend(l, l1)
s.listAppend(l, l1)

nums = [8, 6, 3, 2]
s.addItemToEachItemInList(nums, 1)