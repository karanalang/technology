class Py_CreateDictionaryFrom2Lists:

    def createDictionary(self, l1, l2):

        res = dict(zip(l1, l2))
        print(" res -> ", res)
        res1 = dict(sorted(res.items()))
        print(" res1 sorted -> ", res1)

sol =Py_CreateDictionaryFrom2Lists()
l1 = [3, 4, 6, 5]
l2 = [33,44,66,55]
sol.createDictionary(l1,l2)


