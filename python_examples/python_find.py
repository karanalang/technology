s = 'leetcode'

substr = 'leet'

print(substr in s)

print(" s.find(substr) ", s.find(substr))

print(" count of occurrences of substr in s -> ", s.count(substr))

print(" find index of occurrences of string in string ")

# https://www.geeksforgeeks.org/python-all-occurrences-of-substring-in-string/

import re

test_str = 'applepenapple'
wordDict = ["apple", "pen"]

for w in wordDict:
    ListOfAllOccurrences = re.findall(w, test_str)
    # IndexesOfAllOccurrences = re.finditer(w, test_str)
    ListOfAllStartIndexes = [(i.start(), i.end(), w) for i in re.finditer(w, test_str)]
    allIndexes = [i for i in re.finditer(w, test_str)]

    print(" ListOfAllOccurrences -> ", ListOfAllOccurrences, " IndexesOfAllOccurrences -> ", ListOfAllStartIndexes)
    print(" allIndexes -> ", allIndexes)