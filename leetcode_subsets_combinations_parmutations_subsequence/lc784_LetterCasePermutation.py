# https://www.youtube.com/watch?v=4eOPYDOiwFo
# https://www.youtube.com/watch?v=x2emlQREyWQ&t=335s

from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:

        if not S:
            return []
        res = []

        def dfs(sArr, idx):

            print(" sArr -> ", sArr)
            if idx == (len(S) - 1):
                sArr.append(S[idx])
                tmp = "".join(sArr)
                print(" adding to res -> ", tmp)
                res.append(tmp)
                sArr.pop()
                return

            print(" idx -> ", idx, " sArr -> ", sArr, " S[idx] -> ", S[idx], " isdigit -> ", S[idx].isdigit())

            # sArr.append(S[idx])

            if S[idx].isdigit():
                sArr.append(S[idx])
                dfs(sArr, idx + 1)
                sArr.pop()
            else:
                sArr.append(S[idx].lower())
                dfs(sArr, idx + 1)
                print(" 2.added sArr -> ", sArr)
                sArr.pop()
                sArr.append(S[idx].upper())
                # print(" ")
                dfs(sArr, idx + 1)
                sArr.pop()

            # sArr.pop()

        dfs([], 0)
        print(" res -> ", res)
        return res


sol = Solution()
# S = 'a1b2'
S = 'C'
res = sol.letterCasePermutation(S)
print(" res -> ", res)
