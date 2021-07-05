class Py_LastOccurrenceOfElemInList:

    def getLastInndexOfElemInList_1(self, nums):

        print(" using join & rfind ")
        lastIndex = "".join(nums).rindex('e')
        print(" lastIndex_1 -> ", lastIndex, " type(lastIndex) -> ", type(lastIndex))

    def getLastInndexOfElemInList_2(self, nums):

        print(" using slice + index()")
        reverseIndex = nums[::-1].index('e')
        lastIndex_2 = len(nums)-1-reverseIndex
        print(" lastIndex_2 -> ", lastIndex_2, type(reverseIndex))

    def getLastInndexOfElemInList_3(self, nums):

        print(" using max + enumerate ")
        indexes = [idx for idx, num in enumerate(nums) if num == 'e']
        lastIndex_3 = max(indexes)
        print(" lastIndex_3 -> ", lastIndex_3)


sol = Py_LastOccurrenceOfElemInList()
nums = ['G', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'g', 'e', 'e', 'k', 's']
sol.getLastInndexOfElemInList_1(nums)
sol.getLastInndexOfElemInList_2(nums)
sol.getLastInndexOfElemInList_3(nums)
