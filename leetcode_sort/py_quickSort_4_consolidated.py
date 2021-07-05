# https://www.educative.io/edpresso/how-to-implement-quicksort-in-python
# https://www.youtube.com/watch?v=MZaf_9IZCrc
# https://stackoverflow.com/questions/18262306/quicksort-with-python

class QuickSort:

    def __init__(self, nums):
        self.nums = nums
        print(" input -> ", nums)

    def partition(self, start, end):

        i = start-1 #
        j = start
        pivot = end
        print(" pivot -> ", self.nums[pivot])

        while j < pivot:
            if self.nums[j] < self.nums[pivot]:
                i+=1
                # print(" i -> ", i, " j -> ", j)
                self.swap(i,j)
            j+=1

        self.swap(i+1, pivot)
        print(" nums after swap -> ", self.nums)
        return i+1

    def swap(self, i, j):
        tmp = self.nums[i]
        self.nums[i]=self.nums[j]
        self.nums[j]=tmp

    def quickSort(self, start, end):

        if start >= end:
            return
        else:
            idx = self.partition(start, end)
            print(" idx -> ", idx)
            self.quickSort(start, idx-1)
            self.quickSort(idx+1, end)


# nums=[5, 2, 10, 0, 3]
# nums=[7, 2, 1, 8, 6, 3, 5, 4]
nums = [100, 200, 50, 20, 70, 2000]
sol = QuickSort(nums)
sol.quickSort(0, len(nums)-1)
# idx = sol.partition(0, len(nums)-1) # working fine
# print(" res -> ", sol.nums, " idx -> ", idx)
print(" res -> ", sol.nums)
