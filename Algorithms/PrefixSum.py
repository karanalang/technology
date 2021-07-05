
class PrefixSum:

    def __init__(self, arr):
        self.arr = arr
        self.prefixSum = [arr[0]]
        for i in range(1, len(arr)):
            self.prefixSum.append(self.prefixSum[i-1]+self.arr[i])
        print(" prefixSum -> ", self.prefixSum)




    def brute(self, i, j):

        tmp = 0
        for n in range(i, j+1):
            tmp += self.arr[n]

        return tmp


    def usingPrefixSum(self, i, j):

        return self.prefixSum[j]-self.prefixSum[i-1]


    def usingSegmentTree(self, i, j):
        pass




arr = [1, 2,3 ,8, 0, 9]
sol = PrefixSum(arr)
res1 = sol.brute(2,4)
res2 = sol.usingPrefixSum(2, 4)
print(" res1 -> ", res1, " res2 -> ", res2)