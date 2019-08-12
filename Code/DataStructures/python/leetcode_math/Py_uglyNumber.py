class Solution:
    def isUgly_bruteforce(self, num: int) -> bool:
        if(num == 1):
            return True

        for i in range(2, num + 1):
            if (num % i == 0):
                print(" Factor -> ", i)
                if (self.isPrime(i)):
                    print(" Prime Factor -> ", i)
                    if (i not in [2, 3, 5]):
                        return False

        return True


    def isPrime(self, num):

        for i in range(2,num):
            if(num%i ==0):
                return False

        return True



    def isUgly_2(self, num:int) -> bool:

        while(num > 1):
            if(num%2 == 0):
                num = num//2
            elif(num%3 == 0):
                num = num//3
            elif (num % 5 == 0):
                num = num // 5
            else:
                return False


        return True





sol = Solution()
n = 14
print("bruteForce -> ", sol.isUgly_bruteforce(n))
print(" isUgly_2 -> ", sol.isUgly_2(n))

