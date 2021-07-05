class PythonDictionary_get:

    def dict_usingGet(self, d:dict):

        print(" d.get('A') -> ", d.get('A'))
        try:
            val = d.get('E')
            print(" val -> ", val)

            val1 = d['E']

        except:
            print(" error, Key not present")

        values = d.get
        print(" d.get, all values -> ", values)

        maxKey = max(d, key=d.get)
        print(" maxKey -> ", maxKey)
        print(" d.items() - returns list of items ", d.items())
        print(" d.keys() - list of keys -> ", d.keys())
        print(" list of values -> ", d.values())

        print(" pop item from dict ")
        d.pop('A')
        print(" d after pop ", d)

sol = PythonDictionary_get()
d = {'A':1, 'B':56, 'C':10}
sol.dict_usingGet(d)