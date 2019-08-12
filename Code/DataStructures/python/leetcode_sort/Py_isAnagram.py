from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return False
        return (sorted(list(s)) == sorted(list(t)))


    def isAnagram_1(self, s: str, t: str) -> bool:

        if(len(s) != len(t)):
            return True


    def isAnagram_1(self, s: str, t: str) -> bool:

        return Counter(s) == Counter(t)



soln = Solution()
s = 'anagram'
t = 'nagaram'

print(soln.isAnagram(s, t))