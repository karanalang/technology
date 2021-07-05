class ConvertNumberToBinary_Recursion:

    def convertToBinary_recursion(self, decimal_number):
        if decimal_number == 0:
            return 0
        else:
            return (decimal_number%2 + 10 * self.convertToBinary_recursion(decimal_number//2))


sol = ConvertNumberToBinary_Recursion()
decimal_num = 17
bin_num = sol.convertToBinary_recursion(decimal_num)
print(" binary_num -> ", bin_num)