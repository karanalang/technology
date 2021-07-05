# https://www.educative.io/edpresso/how-to-implement-quicksort-in-python
# https://www.youtube.com/watch?v=MZaf_9IZCrc
# https://stackoverflow.com/questions/18262306/quicksort-with-python

class QuickSort:

    def __init__(self, nums):
        self.nums = nums
        print(" input -> ", nums)

    def partition(self):

        i = -1 #
        j = 0
        pivot = len(self.nums)-1
        print(" pivot -> ", self.nums[pivot])

        while j < pivot:
            if self.nums[j] < self.nums[pivot]:
                i+=1
                # print(" i -> ", i, " j -> ", j)
                self.swap(i,j)
            j+=1


        self.swap(i+1, pivot)

        print(" nums after swap -> ", self.nums)
        # return self.nums

    def swap(self, i, j):
        # print(" before swap -> ", self.nums)
        tmp = self.nums[i]
        self.nums[i]=self.nums[j]
        self.nums[j]=tmp
        # print(" after swap -> ", self. nums)
        # return self.nums

    def quickSort(self):
        pass

# nums=[5, 2, 10, 0, 3]

nums=[7, 2, 1, 8, 6, 3, 5, 4]
sol = QuickSort(nums)
# sol.partition()
print(" res -> ", sol.nums)
