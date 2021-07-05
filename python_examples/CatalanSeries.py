import math

class CatalanSeries:

    def getCatalanNumbersUsingInbuiltFn(self, n):

        res = []

        for i in range(1, n+1):
            print(" i -> ", i)
            cs = int(math.factorial(2*i)/(math.factorial(i+1)*math.factorial(i)))
            res.append(cs)

        return res

    def getCatalanNumber_rec(self, n):

        res = []
        def factorial(i):
            # res = 1
            if i == 1:
                return 1

            i *= factorial(i-1)
            return i

        for i in range(1, n+1):
            res.append(int(factorial(2*i)/(factorial(i+1)*factorial((i)))))

        return res


sol = CatalanSeries()
n = 4
catalanNumber = sol.getCatalanNumbersUsingInbuiltFn(n)
print(" Catalan Number is -> ", catalanNumber)

catalanNumber_rec = sol.getCatalanNumber_rec(n)
print(" catalanNumber using rec -> ", catalanNumber_rec)