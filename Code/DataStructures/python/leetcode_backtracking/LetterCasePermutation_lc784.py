from typing import List

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:



        res = []
        # res.append(S.upper())
        # res.append(S.lower())

        print(res)

        for i in range(len(S)):
           if(S[i].upper() != S[i].lower()):


                tmpUpper1 = ''.join(S[0::(i-1)])
                tmpUpper2 = tmpUpper1.join(S[i].upper())
                tmpUpper3 = tmpUpper2.join(S[i+1:])

                print(" tmpUpper1 -> ", tmpUpper1, " tmpUpper2 -> ", tmpUpper2, " tmpUpper3 -> ", tmpUpper3)

                # tmpLower= S[::(i-1)].join(S[i].lower()).join(S[(i+1)::])
                res.append(tmpUpper3)
                # res.append(tmpLower)

        return res

    # using divide & conquer
    def letterCasePermutation_2(self, S:str) -> List[str]:

        res = []
        if(len(S) == 0):
            return []

        def backtrack(S, step, curr, res):

            # end of the String
            if(step == len(S)):
                res.append(curr)
                return

            # when we have a number
            if(S[step].lower() == S[step].upper()):
                backtrack(S, step+1, curr + S[step], res)
            else:

            # if(S[step].lower() != S[step].upper()):
                backtrack(S, step+1, curr+S[step].lower(), res)
                backtrack(S, step+1, curr+S[step].upper(), res)


        backtrack(S, 0, "", res)

        return res


    def letterCasePermutation_3(self, S:str) -> List[str]:

        # if(len(S) == 0):
        #     return []

        if(len(S) == 1):
            if(S.lower() == S.upper()):
                return S
            elif (S.lower() == S):
                    return [S, S.upper()]
            else:
                return [S, S.lower()]

        mid = len(S)//2

        left = self.letterCasePermutation_3(S[:mid])
        right = self.letterCasePermutation_3(S[mid:])

        res = [x + y for x in left for y in right]
        return res




soln = Solution()
S = "a1b2"
res = soln.letterCasePermutation_3(S)
print("all letter case permutations -> ", res)