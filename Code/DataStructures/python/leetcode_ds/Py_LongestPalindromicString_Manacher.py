class Solution:
    def longestPalindrome(self, s: str) -> str:
        # return None
        T = '#'.join('^{}$'.format(s))
        print(" T -> ", T)
        n = len(T)
        print(" n -> ", n)
        P = [0] * n
        print(" P -> ", P)
        C = R = 0
        # C -> Center of the main Palindrome
        # R -> Right boundary
        # mirr - mirror of the P[i] -> P[2*C -1]
        for i in range(1, n-1):
            P[i] = (R > i) and min(R -i, P[2*C -1]) # equals to i' = C - (i - C)
            print(" P[i] -> ", P[i])
            # Attempt to expand palindrome centered at i
            while(T[i+1+ P[i]] == T[i-1-P[i]]):
                P[i] += 1


            # if Palindrome centered at i expand past R,
            # adjust Center based on expanded Palindrome
            if (i + P[i] > R):
                C, R = i, i + P[i]
                print(" C -> ", C, " R -> ", R)


        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex - maxLen)//2]


    def longestPalindrome2(self, s):
        T = '#'.join('^{}$'.format(s))
        print(" T -> ", T)
        n = len(T)
        print(" n -> ", n)
        P = [0] * n
        print(" P -> ", P)
        C = R = 0
        for i in range(1, n-1):
            mirr = 2*C -1
            if(i < R):
                P[i] = min(R-i, P[mirr])

            while(T[i + (i + P[i])] == T[i - (1 + P[i])]):
                P[i] =+ 1

            if(i + P[i] > R):
                C = i
                R = i + P[i]


        return P



s = Solution()
longestPalindrome = s.longestPalindrome2("aba")
print(" longestPalindrome -> ", longestPalindrome)


