# https://www.geeksforgeeks.org/python-get-key-with-maximum-value-in-dictionary/
# https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
import operator

class PythonDict_GetKeyWithMaxValue:

    def dict_getKeyWithMaxValue_1(self, d:dict):
        print(" using max function")
        maxVal = max(d, key=d.get)
        print(" maxVal -> ", maxVal)

    def dict_getKeyWithMaxValue_2(self, d:dict):
        print(" using operator")
        d_items = d.items()
        maxV1 = max(d_items, key=operator.itemgetter(0))[0]
        maxV2 = max(d_items, key=operator.itemgetter(1))[0]
        print(" maxV1 -> ", maxV1, " maxV2 -> ", maxV2)


    def dict_getKeyWithMaxValue_3(self, d: dict):
        print(" get list of keys, values, and get index of max value, the use that index to get corresponding key in list(keys")
        d_values = list(d.values())
        d_keys = list(d.keys())

        max_d_value = max(d_values)
        index_maxval = d_values.index(max_d_value)
        print(" d_keys[index_maxval] -> ", d_keys[index_maxval])

    def dict_getMaxValueAndKey(self):
        pass



sol = PythonDict_GetKeyWithMaxValue()
d = {'A':121, 'B':45, 'C':10, 'D':119}
# sol.dict_getKeyWithMaxValue_1(d)
# sol.dict_getKeyWithMaxValue_2(d)
sol.dict_getKeyWithMaxValue_3(d)
