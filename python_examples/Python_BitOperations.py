# https://www.geeksforgeeks.org/python-bitwise-operators/

class Python_BitOperations:

    def bitwise_AND(self, a, b):

        print(' bitwise operator - AND -> ', a & b)

    def bitwise_OR(self, a, b):
        print(' bitwise operator - OR -> ', a | b)

    def bitwise_NOT(self, a, b):
        one_1 = ~a

        print(" bin(a) -> ", bin(a), " a -> ", a, " ones complement of a -> ", one_1,' format(a, b)', format(a, 'b') )

        print(' 1.bitwise operator - NOT ones complement of a -> ', ~a, " 2s complement of a i.e.one's complement + 1-> ", ~a+1)
        print(' 1.bitwise operator - NOT ones complement of b -> ', ~b, " 2s complement of b i.e.one's complement + 1-> ", ~b+1)

    def bitwise_XOR(self, a, b):

        xor = a ^ b
        print(' bitwise_XOR : <- a -> ', a, ' <- b -> ', b, 'a ^ b -> ', xor)

    def bitwise_leftShift_multiplyBy2(self, a):

        ls = a << 1
        print(" a -> ", a , " after left shift 1 -> ", ls)

        ls1 = a << 2
        print(" a -> ", a , " left shift 2 times -> ", ls1)

    def bitwise_rightShift_divideBy2(self, a):

        rs1 = a >> 1
        print(" a -> ", a, " right shift once -> ", rs1)

        rs2 = a >> 2
        print(" a -> ", a, " right shift 2 times -> ", rs2)


    def bitwise_NegativeNumber(self, n):

        print(" n -> ", n , " binary of -ve num, format -> ", format(n, 'b'), "  binary of -ve num, bin ->  ", bin(n))



    def convertToBinary_InBuiltFunction(self, n):

        print(" bin(n) -> ", bin(n), " type(bin(n)) -> ", type(bin(n)))
        print(" format(n) ", format(n, 'b'), " type(format(n, 'b')) -> ", type(format(n, 'b')))



sol = Python_BitOperations()
a = 5
# print(" converting a to bin -> ", bin(a)[2:])
b = 2
# print(" converting b to bin -> ",bin(b)[2:])

sol.bitwise_AND(a,b)
# sol.bitwise_OR(a,b)
# sol.bitwise_NOT(a, b)
#
# sol.bitwise_XOR(a, b)
# sol.bitwise_leftShift_multiplyBy2(a)
# sol.bitwise_rightShift_divideBy2(a)
#
# sol.bitwise_NegativeNumber(-5)

# sol.convertToBinary_InBuiltFunction(a)
# sol.convertToBinary_InBuiltFunction(b)

a = 10
print(a << 1 << 3)



