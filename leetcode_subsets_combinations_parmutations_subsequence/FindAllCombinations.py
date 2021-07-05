# https://www.geeksforgeeks.org/print-all-possible-combinations-of-r-elements-in-a-given-array-of-size-n/

class FindAllCombinations:

    def allCombinations_iterative(self, nums):

        res = []

        for i in range(len(nums)):
            for j in range(i, len(nums)+1):
               print(" i -> ", i, " j -> ", j)
               tmp = nums[i:j]
               print(" tmp -> ", tmp)
               res.append(tmp)

        return res

    def allCombinations_recursive(self, nums):
        pass

sol = FindAllCombinations()
nums = [1, 2, 3]
res=sol.allCombinations_iterative(nums)
print(" res -> ", res)
# print(" convert to set -> ", set(res))
