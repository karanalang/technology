from typing import List

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:

        if(N == 1):
            if(len(trust) == 0):
                return 1
            else:
                return -1


        first = []
        second = []
        for i in range(len(trust)):
            print(" 1st item in list -> ", trust[i][0], " 2nd item in List -> ", trust[i][1])
            first.append(trust[i][0])
            second.append(trust[i][1])

        print(set(second) - set(first))
        set_ = set(second) - set(first)
        if(len(set_) > 0):
            possibleJudge = set_.pop()
            countOfJudge = second.count(possibleJudge)
            print("countOfJudge -> ", countOfJudge)
            if(countOfJudge == (N-1)):
                return possibleJudge
            else:
                return -1
        else:
            return -1


    def findJudge(self, N: int, trust: List[List[int]]) -> int:

        if (N == 1 & (len(trust) == 0)):
            return 1

        first = []
        second = []
        for i in range(len(trust)):
            first.append(trust[i][0])
            second.append(trust[i][1])

        diff = [i for i in second if i not in first]
        if(len(set(diff)) == 1 and (len(diff) == (N-1))):
            return diff[0]
        else:
            return -1







soln = Solution()
l = [[1,2], [2,3]]
judge = soln.findJudge(3,l)
print(" judge -> ", judge)
