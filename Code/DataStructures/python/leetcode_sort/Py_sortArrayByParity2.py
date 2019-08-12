from typing import List

class Solution:
    def sortArrayByParityII_2Pass(self, A: List[int]) -> List[int]:

        res = [0] * len(A)
        evenindex = 0
        oddindex = 1
        for i in range(len(A)):
            if (A[i] % 2 == 0):
                res[evenindex] = A[i]
                evenindex = evenindex + 2
            else:
                res[oddindex] = A[i]
                oddindex = oddindex + 2

        return res




    def sortArrayByParityII_1Pass_1(self, A: List[int]) -> List[int]:

        # res = [0] * len(A)
        evenNumber_OddPl = -1
        oddNumber_EvenPl = -1

        for i in range(len(A)):
            if((i%2 == 0) & (A[i]%2 != 0)):
                oddNumber_EvenPl = i
            if((i%2 != 0) & (A[i]%2 == 0)):
                evenNumber_OddPl = i

            # print(" oddNumber_EvenPl -> ", oddNumber_EvenPl, " evenNumber_OddPl -> ", evenNumber_OddPl)
            if((oddNumber_EvenPl != -1) & (evenNumber_OddPl != -1)):
                A[oddNumber_EvenPl], A[evenNumber_OddPl] = A[evenNumber_OddPl], A[oddNumber_EvenPl]

        return A

    def sortArrayByParityII_1Pass(self, A: List[int]) -> List[int]:

        print(" <- sortArrayByParityII_1Pass -> ")
        j = 1
        for i in range(0, len(A),2):
            print(" A[i]%2 -> ", A[i]%2)
            print(" A[i]%2 == 0 -> ", (A[i]%2 == 0))
            # if(A[i]%2 == 0):
            #     while(A[j]%2 == 0):
            #         j += 2
            if (A[i] % 2 ==0):
                while (A[j] % 2 ==0):
                    j += 2

                print(" A[i] -> ", A[i], " A[j] -> ", A[i], " i -> ", i, " j -> ", j)
                A[i], A[j] = A[j], A[i]


        return A




s = Solution()
l = [4,2,5,7]
lSorted = s.sortArrayByParityII_1Pass(l)
print(lSorted)

# lSorted1 = s.sortArrayByParityII_2Pass(l)
# print(lSorted1)