class Solution:
    def countSubString(self, s) -> int:
        """
        :type s:  String
        :return: int
        """

        def isPalindrome(i, j) -> bool:
            return s[i:j+1] == s[i:j+1][::-1]

        i =0
        count = 0
        slen = len(s)

        while (i < slen):
            j = slen -1
            while (j >= i):
                if(isPalindrome(i, j)):
                    count += 1
                j -= 1

            i += 1

        return count



    def countString2(self, s):

        '''

        while (i < len(s) -1) :
        within while loop :
            call inner method isPalin(i, j) where i = 0, j = len(s) -1
            within isPalin - check if the subArray (i.e s[i:j] is a Palindrome,
            decrease j by 1

        increase i by 1

        ou
        increase s by 1, decrease j by 1

        :param s:
        :return:
        '''

        count = 0
        slen = len(s)
        i = 0

        def isPalin(i, j) -> bool:
            print(" i -> ", i, " j -> ", j, )
            return s[i:j+1] == s[i:j+1][::-1]

        while (i < slen):
            j = slen -1

            while(j >= i):
                isPalin_ = isPalin(i, j)
                print(isPalin_)
                if(isPalin_):
                    print(" IT is Palindrome ")
                    count += 1
                j -= 1 # from s[i, slen] to s[i, i-1]

            i += 1

        return count


s = Solution()
one = s.countSubString("ab")
print(" one -> ", one)


two = s.countString2("ab")
print(" two -> ", two)


