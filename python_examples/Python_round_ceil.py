# https://www.knowledgehut.com/blog/programming/python-rounding-numbers
import math

class Python_ceil_round:

    def usingCeil(self, n:float):
        print(" rounding to upper Integer -> ", math.ceil(n))


    def usingRound(self, n:float):

        print(" using round -> ", round(n))

        print(round(5.465, 2))
        print(round(5.465, 3))
        print(round(5.476, 2))
        print(round(5.4768, 2))




s = Python_ceil_round()
# s.usingCeil(1.2)
# s.usingCeil(2.8)
# s.usingCeil(5.1)
# s.usingRound(1.2)
# s.usingRound(1.5)
# s.usingRound(2.49)
s.usingRound(2.51)


