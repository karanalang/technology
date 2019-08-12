from typing import List
import sys

class Solution:

    def test(self):
        print("hello")

    def listArrays(self, nums:List[int]):
        print("listArrays -> ", nums)
        for w in range(1, len(nums)+1):
            print(" len(nums) - w + 1")
            for i in range(len(nums)-w+1):
                print("i -> ", i, " w -> ", w, " w+i -> ", (w+i))
                print(nums[i:w+i])

    # https: // stackoverflow.com / questions / 41576911 / list - all - contiguous - sub - arrays
    # def allSubArrays(L, L2=None):
    #     if L2 == None:
    #         L2 = L[:-1]
    #     if L == []:
    #         if L2 == []:
    #             return []
    #         return allSubArrays(L2, L2[:-1])
    #     return [L] + allSubArrays(L[1:], L2)


    def listArrays2(self, nums:List[int]) -> int:
        for i in range(0, len(nums)):
            for j in range(len(nums)-i+1):
                print(nums[i:i+j])



    def listArrays3(self, nums:List[int]) -> int:
        for i in range(0, len(nums)):
            # print(" i -> ", i)
            for j in range(i+1, len(nums)+1):
                # print(" j -> ", j)
                # print(nums[i:j])
                yield nums[i:j]




l = [1, 2, 3]

# print(l[0:0])
# print(l[0:1])
# print(l[0:2])
#
# print(l[1:2])
# print(l[1:3])
# print(l[2:3])


s = Solution()
yieldGenerator = s.listArrays3(l)

maxSum = (-sys.maxsize -1)

for i in yieldGenerator:
    if(maxSum < sum(i)):
        maxSum = sum(i)
    # print(" from yield -> ", i)

print(" maxSum is -> ", maxSum)

# print(" y-> ", y)
# if not None:
#     print(next(y))



# s = Solution()
# s.listArrays2(l)

# for i1 in range(len(l)):
#     print("i1 -> ", i1)
#     # print(l[i1:0])
#     print(l[i1:i1+2])

# def CallingFromMain():
#     print(" Calling from main")
#
#
# if __name__ == '__main__':
#     CallingFromMain()


# for i in range(4):
#     print(" ranges(4) -> ", i)


"""
expected [1],[2], [1,2]

for i = 0, j = 0 upto 2




"""