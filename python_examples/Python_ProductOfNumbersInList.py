# https://stackoverflow.com/questions/2104782/returning-the-product-of-a-list/9114648
# https://www.geeksforgeeks.org/python-multiply-numbers-list-3-different-ways/
import numpy as np
from functools import reduce

class Py_ProductOfNumbersInList:

    def getProdOfNumbersInList_brute(self, nums):

        prod = 1
        for n in nums:
            prod *= n

        print(" getProdOfNumbersInList_brute, product -> ", prod)

    def getProdOfNumbersInList_numpy(self, nums):
        prod = np.product(nums)
        print(" Product of number susing numpy -> ", prod)
        prod1 = np.prod(nums)

        print(" product using numpy1 -> ",prod1)


    def getProdOfNumbersInList_reduce(self, nums):

        prod = reduce(lambda x,y:x*y, nums)
        print(" prod using functools.reduce -> ", prod)



    # def getProdOfNumbersInList_map(self, nums):
    #
    #     prod = map(lambda x,y:x*y, nums)
    #     print(" product ogf list items using map -> ", prod)

sol = Py_ProductOfNumbersInList()
nums = [2, 3, -1, 4]
sol.getProdOfNumbersInList_brute(nums)
sol.getProdOfNumbersInList_numpy(nums)
sol.getProdOfNumbersInList_reduce(nums)
# sol.getProdOfNumbersInList_map(nums)