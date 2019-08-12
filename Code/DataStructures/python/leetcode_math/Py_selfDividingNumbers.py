from typing import List

class Solution:

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:

        sd_number = []

        for i in range(left, right +1):
            self.checkSelfDividing(i, sd_number)
            # print("i -> ", i)

        print(" sd_number is -> ", sd_number)
        return sd_number

    def checkSelfDividing(self, n: int, sd_number: List[int]):

        origN = n
        if(n < 10):
            sd_number.append(n)
            return sd_number

        while(n != 0):
            div = n%10
            if(div != 0):
                if(origN%div != 0):
                    return sd_number
                else:
                    n = int(n/10)
            else:
                return sd_number

        sd_number.append(origN)
        return sd_number



s1 = Solution()
s1.selfDividingNumbers(1, 22)
