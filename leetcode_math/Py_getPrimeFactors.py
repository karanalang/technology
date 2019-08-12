class GetPrimefactors:
    def getAllfactors(self, num: int):

        for i in range(2, num+1):
            if(num%i == 0):
                print(" Factor -> ", i)
                if(self.isPrime(i)):
                    print(" Prime Factor -> ", i)


        # return None


    def isPrime(self, num):

        for i in range(2,num):
            if(num%i ==0):
                return False

        return True


gpf = GetPrimefactors()
gpf.getAllfactors(6)