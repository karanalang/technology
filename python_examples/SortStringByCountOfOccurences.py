# https://stackoverflow.com/questions/23429426/sorting-a-list-by-frequency-of-occurrence-in-a-list
from itertools import chain, repeat

from collections import Counter

class SortStringByCountOfOccurrences:

    def sortString(self, S:str):

        S = str(sorted(S))
        print(" sorted S -> ", S)


    def sortStringByCount(self, S):

        sortedStr = sorted(S, key=Counter(S).get)
        print(" sortedString by count of occurrenecs ", sortedStr)

        sortedStr_ReverseOrder = sorted(S, key=Counter(S).get, reverse=True)
        print(" sorted String by count of occurrences, reverse = true -> ", sortedStr_ReverseOrder)

    def sortStringByCount_2(self, S):

        for items, cnt in Counter(S).most_common():
            print(" %s:%d "% (items,cnt))

        sortedStr = [item for items, cnt in Counter(S).most_common() for item in [items]*cnt]
        print(" sortedStrByCnt_2 -> ", sortedStr)

    def sortStringByCount_3(self, S):

        sortedStr_3 = list(chain.from_iterable(repeat(i,c) for i,c in Counter(S).most_common()))
        print(" sortedStr_3 -> ", sortedStr_3)



c = Counter()
c.most_common(10)


sol = SortStringByCountOfOccurrences()
S = 'aaabcccccdddefff'
sol.sortString(S)
sol.sortStringByCount(S)
# sol.sortDict({'a':2, 'b':3, 'c':1})
sol.sortStringByCount_2(S)
sol.sortStringByCount_3(S)