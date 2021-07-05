# https://www.geeksforgeeks.org/find-median-of-list-in-python/

from statistics import median


l = [4, 5, 8, 9, 10, 17]

print(" sum of l -> ", sum(l), " sum/len(l) -> ", sum(l)/len(l))

medianOfList = median(l)
print(" median of l -> ", medianOfList)

l1 = [1, 6, 8, 10, 14]

print(" for list with len(num) = odd, median -> mid number ", median(l1))
mid = len(l1)//2
print(" middle number of sorted list with Odd number of elements -> ", l1[mid])

print(" for list of even number of items in list, median is avarage of mid & mid-1 numbers")
l2 = [1, 6, 8, 10]
mid1 = len(l2)//2
mid2 = mid1-1
print(" median of mid1 & mid2 -> ", (l2[mid1] + l2[mid2])/2, " statistics,median(l2) -> ", median(l2))


print(" Median of even number list, Method 2")
# l3 = [1, 6, 8, 10]
mid = len(l2)//2
print("mid -> ", mid, " ~mid -> ", ~mid+1)
median_2 = (l2[mid] + l2[~mid])//2
print(" median_2 -> ", median_2)