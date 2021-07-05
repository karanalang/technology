# https://www.geeksforgeeks.org/python-program-to-covert-decimal-to-binary-number/

class Py_ConvertToBinary:

    def convertDecimalToBinary(self, n:float):

        binNumber = bin(n).replace('0b','')
        print(" binNumber-> ", binNumber)


    def convertDecimalToBin_rec(self, n:float):
        pass




sol = Py_ConvertToBinary()
n = 7
n1 = 9
n2 = 100
sol.convertDecimalToBinary(n)
sol.convertDecimalToBinary(n1)
sol.convertDecimalToBinary(n2)