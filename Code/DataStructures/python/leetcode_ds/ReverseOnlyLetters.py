from typing import List


class ReverseOnlyLetters():
    def reverseOnlyLetters(self, S:str) -> str:
        letters = [c for c in S if c.isalpha()]
        print(letters)
        ans = []
        for c in S:
            if (c.isalpha()):
                ans.append(letters.pop())
                # print(c, " - is Alpha")
            else:
                ans.append(c)
                # print(c, " - is not Alpha")

        return "".join(ans)


r = ReverseOnlyLetters()
reversed = r.reverseOnlyLetters("Hello-")
print(reversed)


S = "Hello1%%^&!"

# letters = [c for c in S if c.isalpha()]
# print(" letters -> ", type(letters), letters)


