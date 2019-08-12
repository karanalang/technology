from typing import List

class Solution:
    def diStringMatch(self, S: str) -> List[int]:

        maxVal = len(S)
        res = [0] * (maxVal+1)
        minI = 0
        maxD = maxVal



        for i in range(0, maxVal):

            if (S[i] == 'I'):
                res[i] = minI
                minI += 1
            else:
                res[i] = maxD
                maxD -= 1

        print(" 1. res -> ", res)
        print(" S[maxVal-1] -> ", S[maxVal-1], " maxD -> ", maxD, " minI -> ", minI)

        if(S[maxVal-1] == 'D'):
            res[maxVal] = (maxD)
        else:
            res[maxVal] = (minI)

        return res






soln = Solution()
s = 'III'
s1 = 'IDID'
res = soln.diStringMatch(s1)
print(res)