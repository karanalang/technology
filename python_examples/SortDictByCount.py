# https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value

class SortDictByCount:

    def sortDict(self, d:dict):

        sortedDictByValue = sorted(d.items(), key=lambda item:item[1], reverse=True)
        print(" sortedDictByValue -> ", sortedDictByValue)

        sortedDictByKey = sorted(d.items())
        print("sorted dict by key -> ", sortedDictByKey)

        for key, value in d.items():
            print(" key -> ", key, " value -> ", value)

        for item in d.items():
            print(" item -> ", item)


sol = SortDictByCount()
d = {'a':3, 'b':123, 'c':2, 'd':0.1}
sol.sortDict(d)