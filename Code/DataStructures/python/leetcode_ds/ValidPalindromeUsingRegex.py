import re

class Solution():
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('\W+','', s).lower()
        print(" s => ", s)
        return s == s[::-1]



s = Solution()
b = s.isPalindrome("aa pqrst .. iii")
print(b)