from typing import List

class Py_IndexOfItemInList:

    def getIndexInList(self, nums:List[int], elem):

        # indexOfElem = nums.index(elem)
        # print(" index is -> ", indexOfElem)
        indexes = [idx for idx, num in enumerate(nums) if num == elem]
        lenArr = indexes[1]-indexes[0]+1
        print(indexes, " lenArr -> ", lenArr)


sol = Py_IndexOfItemInList()
nums = [1, 2, 2, 3, 1]
sol.getIndexInList(nums, 1)

