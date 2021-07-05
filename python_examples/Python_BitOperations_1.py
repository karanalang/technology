class Python_BitOperations_1:

    def bitoperation_leftshift_multiplyBy2(self, a):

            print(" input a -> ", a)
            print(a << 1 << 1 == a << 2)
            print(" divide by 2**0 ", (a >> 0), " multiply by 2**0 -> ", a << 0)
            print(" multiply by 2**1 -> ", a << 1, " divide by 2**1 -> ", (a >> 1))



sol = Python_BitOperations_1()
a = 10
sol.bitoperation_leftshift_multiplyBy2(a)

