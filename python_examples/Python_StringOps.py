import re

class Python_StringOps:

    def removeSpaces(self, s):
        str1 = s.replace(' ','')
        print(" str after removing spaces -> ", str1)

    def splitString(self, s:str, splitCh:str):
        # str.
        res = s.split(splitCh)
        print(" res -> ", res)

    def extractNumbersFromString(self, s:str):

        # s = s.split()
        # print(" s, after s.split() ", s)
        allNos = [int(i) for i in s.split('+') if i.isdigit()]
        print(" allNos ->", allNos)

    def extractNumbersFromString_2(self, s: str):
        res = re.findall(r'\d+', s)
        print(" res -> ", res, " type(res) -> ", type(res))

    # loop through the digits, till you find the non-integer
    def extractNumbersFromString_3(self, s: str):
        num = 0
        allNos = []

        for i in s:
            # print(" i -> ", i)
            if i.isdigit():
                num = num*10+int(i)
            else:
                if num != 0:
                    allNos.append(num)
                    num=0
        print(" after parsing, allNos -> ", allNos)


        # for


sol = Python_StringOps()
s = " hello how ru ?  "
sol.removeSpaces(s)
str1 = "hello$there"
sol.splitString(str1, '$')
s2 = '2+3+9'
sol.extractNumbersFromString(s2)
sol.extractNumbersFromString_2(s2)
s3='23*(54-45)'
sol.extractNumbersFromString_3(s3)