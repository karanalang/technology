class Solution:
    def longestPalindrome1(self,s) -> bool:

        max_p = ''
        i = 0
        slen = len(s)

        def isPalindrome(i, j) -> bool:
            return s[i:j+1] == s[i:j+1][::-1]


        while(i < slen):
            j = slen -1
            while (j >= i):
                print(" subbstring -> ", s[i:j])
                if(isPalindrome(i, j)):
                    if(len(s[i:j+1]) > len(max_p)):
                        max_p = s[i:j+1]
                j -= 1
            i += 1

        return max_p


    def longestPalindrome_dp_cnt(self,s) -> str:

        str = self.lps(s, 0, len(s)-1)
        return str



    def lps(self, s, i, j):
        # is there is only one character
        if(i == j):
            return 1

        # if there are only 2 characters, and both are same
        if((s[i] == s[j]) & (i + 1 == j)):
            return 2

        # if the first & last characters match
        # 2 is added, since the length of max
        if(s[i] == s[j]):
            # return self.lps(s, i+1, j-1) + 2
            return self.lps(s, i + 1, j - 1)

        # if the first & last characters donot match
        if (s[i] != s[j]):
            return max(self.lps(i+1, j), self.lps(i, j-1))


s = Solution()

input_ = '"1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111"'
longestP_cnt = s.longestPalindrome_dp_cnt(input_)
print("longestP -> ", longestP_cnt)




longestP_str = s.longestPalindrome_dp_str(input_)
print("longestP -> ", longestP_str)
