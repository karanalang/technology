class CheckPalindrome:

    def isPalindrome(self, s):

        s = s.lower().replace(' ','')
        return s == s[::-1]




p = CheckPalindrome()
s1 = 'A Santa Lived As a Devil At NASA'
print(s1)
print(' check if palindrome -> ', p.isPalindrome(s1))
