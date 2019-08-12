from typing import List

class Solution:
    def maximumProduct2(self, nums: List[int]) -> int:

        len_ = len(nums)
        prod = 1
        if(len_ > 3):
            numsSorted = sorted(nums, reverse=True)
            print(numsSorted)
            for i in range(3):
                prod = prod * numsSorted[i]
        else:
            for i in range(len_):
                prod = prod * nums[i]


        return prod


    def maximumProduct(self, nums:List[int]) -> int:

        numSorted = sorted(nums, reverse=True)
        len_ = len(nums)
        if(len == 3):
                return numSorted[0] * numSorted[1] * numSorted[2]
        else:
            return max((numSorted[0] * numSorted[1] * numSorted[2]), (numSorted[0]*numSorted[len_ -1]*numSorted[len_ -2]))


# Time Complexity -> O(n log n) - to sort the nums array
# Space Complexity -> O(log n) -> to sort the nums array

s = Solution()
nums = [-4,-3,-2,50,60]
prod = s.maximumProduct(nums)
print(prod)
