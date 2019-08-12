class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # return str(int(num1) + int(num2))
        # s = str(self.convertToInt(num1) + self.convertToInt(num1))
        s = str(self.convertToInt(num2))
        print("s => ", s)
        return s

    def convertToInt(self, num:str) -> int:

        lenNum = len(num)
        print(" lenNum -> ", lenNum, " num -> ", num)
        revList = list(num)[::-1]
        print(" list reversed -> ", revList)
        tempInt = 0
        for i in range(0, lenNum):
            print(" i -> ", 10**i, " revList[i] -> ", revList[i])
            tempInt += int(revList[i]) * (10**i)

        print(" tempInt -> ", tempInt)
        return tempInt


    def addString2(self, num1:str, num2:str):

        d = {'0':1, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}

        result1 = 0
        result2 = 0

        for c in num1:
            print(" c -> ", c, " d[c] -> ", d[c])
            result1 = result1 * 10 + d[c]
            print("result1 -> ", result1)

        for c in num2:
            result2 = result2 * 10 + d[c]
            print(" result2 -> ", result2)

        print(result1 + result2)
        return str(result1 + result2)



s = Solution()
# s.addStrings("0", "9")
s.addString2("123","11")