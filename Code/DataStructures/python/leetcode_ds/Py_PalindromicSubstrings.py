class Solution:
    def countSubstrings(self, s: str) -> int:

        count = 0
        subStr = self.listAllConguousSubArrays(s)

        for i in subStr:
            if(i == i[::-1]):
                count += 1

        return count


    def listAllConguousSubArrays(self,s):

        l = list(s)
        for i in range(len(l)+1):

            for j in range(i+1, len(l)+1):
                yield l[i:j]



s = Solution()
s1 = 'abc'
# s.countSubstrings(s1)

longStr = "dbabcccbcdbbbadabbdabaabcbbabaacdadcdbbbbdddbcbbbcbcabacacdaadaadcdccbacdaadadcbaacabbddabdadcabbccadacadaaacbbddaaababacaabbbacaccbcbbabddbbcccaaacbcdcabcbacdbddcdcadaaadcbccbbcabbcbdaadcbddaacacdadacbbdabcdcdadccaccdbdddddcabdbcdbaadacadadbabdcdbbadaacdbadcdabdbbcabbbdaacaaaaadcaabaaaadabaaddcaabdddcbcadcbdbbdbcbcdbadcadacbbcdccddaccccacbacaacbbdadadcacabdabadbbcdbcaaccdbdcabcadbacbccddbabbdacbcbbcbcabcacdaacccaadcdbdccabcaaacaddadcabacdccaaaddaaadbccdbbcccdddababcdbcddcbdddbbbdaadaccbcaabbcbdbadbabbacdbbbdaaccdcabddacadabcccacdabacbcdbcbdabddacacbdbcaacacaabbaaccddabaadbbaabaddbcacbacdbbbacdccabbcdbbbdbdbbcacabdddbdbaaabbcdcbabcbbbccdcdcdcaaddadccbabbacaddcaddcadcdccaccacabbaababdbbcbdcdccccccdadbdbdcdbdadcdcacdaabaacabaacdacdbaaccadbcddbdccabbcabcadcbdadbcdadbbbccacbcbbcaaaabdacbadacaadcadaacdacddcbbabdacacaabccdaccbbcbbcbcaacdabdcbcdbccdbcbcbddaacdacaaaddcaddcadccacbaddbbbccbbbcbbcbadcabbccbbaadaacacabddbdbddcadbdaaccadbcccabdcdbadbbacbcbbcdcabcddcddddabddbdabdcabdbdbbbcdbcdabbdcb"

countOfPalindromes = s.countSubstrings(longStr)
print(" cpunt of Palindromes -> ", countOfPalindromes)

# count = 0
# for i in subArr:
#     # if(i = i[::-1]):
#     print(" subArr is -> ", i)
#     if(i == i[::-1]):
#         count += 1
# print(" total number of Palidromes is -> ", count)