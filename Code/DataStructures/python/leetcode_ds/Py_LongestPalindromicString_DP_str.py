class Solution:

    def longestPalindromicString(self, s: str) -> str:

        len_ = len(s)
        print(" len_ ", len_)
        max_len = 1
        palindromeBeginsAt = 0
        palindrome = [[False] * len_  for i in range(0, len_)]
        print(palindrome)

        for i in range(0, len_):
            for j in range(0,len_):
                if(i == j):
                    palindrome[i][j] = True  # setting to True for all


        for i in range(0, len_-1):
            print(" i -> ", i)
            if(s[i] == s[i+1]):
                palindrome[i][i+1] = True
                palindromeBeginsAt = i
                print(" palindromeBeginsAt -> ", palindromeBeginsAt)
                max_len = 2

        print(" 2. palindrome -> ", palindrome)

        # finding palindromes of length 3 to n and saving the longest
        for curr_len in range(3, len_):
            for i in range(0, len_-curr_len +1):
                j = i+ curr_len -1
                if((s[i] == s[j]) & palindrome[i+1][j-1]):
                    palindrome[i][j] = True
                    palindromeBeginsAt = i
                    max_len = curr_len
                    print(" max_len -> ", max_len)



        print(" palindromeBeginsAt -> ", palindromeBeginsAt)
        return s[palindromeBeginsAt:max_len+1]
        # 1 len palindrome
        # if(len(s) == )


        print(" palindrome ", palindrome)


    def lps(self, s, i, j):

        # when i == j
        if(i == j):
            return s

        # 2 string
        if(s[i] == s[j] & (i+1 == j)):
            return s


        # if first & last letters match
        # from 2


    def longest_pal(self, str):
        n = len(str)

        # initialize Opt Table
        Opt = [[0 for i in range(n)] for j in range(n)]

        # Opt of single char is 1
        for i in range(n):
            Opt[i][i] = 1

        # Opt for adjacent chars is 2 if same, 1 otherwise
        for i in range(n - 1):
            if str[i] == str[i + 1]:
                Opt[i][i + 1] = 2
            else:
                Opt[i][i + 1] = 1


        # we now define sil as (s)substring (i)interval (l) length of the
        # interval [i,j] --- sil=(j-i +1) and j = i+sil-1

        # we compute Opt table entry for each sil length and
        # starting index i

        for sil in range(2, n + 1):
            for i in range(n - sil + 1):
                j = i + sil - 1
            if (str[i] == str[j]):
                Opt[i][j] = Opt[i + 1][j - 1] + 2;
            else:
                Opt[i][j] = max(Opt[i][j - 1], Opt[i + 1][j])

        return Opt[0][n - 1]


s = Solution()
# s.longestPalindromicString("abba")
longPalindrome = s.longest_pal("abba")
print(" longest Palindrome ", longPalindrome)


# longPalindrome_dp = s.longestPalindromicString("babababab")
longPalindrome_dp = s.longestPalindromicString("abba")
print(" longPalindrome -> ", longPalindrome_dp)