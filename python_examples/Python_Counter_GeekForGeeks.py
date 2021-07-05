from collections import Counter

class Python_Counter:

    def py_Counter(self):

        z = ['blue', 'red', 'yellow', 'blue', 'red']
        col_counter = Counter(z)
        print(col_counter, type(col_counter))
        print(" col_counter.values() ->", col_counter.values())

        col = ['blue', 'red']
        for c in col:
            print(c, ' - ', col_counter[c])

        coun = Counter(a=1, b=2, c=3)
        print(" coun -> ", coun, ' <- list of elements -> ', list(coun.elements()), " values -> ", list(coun.values()))

        coun1 = Counter(aa=22, bb=333, cc=862)
        for letter, count in coun1.most_common(2):
            print('%s : %d' % (letter, count))


s = Python_Counter()
s.py_Counter()