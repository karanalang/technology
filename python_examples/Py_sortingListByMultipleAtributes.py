ll = [[5,2], [5,0],[1,1],[3,7], [4,4]]

print(" sorting in AscendingOrder, by 0th element, if 0th element is same, by 1st element")
ll.sort(key=lambda x:(x[0], x[1]))

print(" ll -> ",ll)

print(" sorting in AscendingOrder by 0th element, if 0th element is same, by 1st element but in descending order")
ll1 = [[5,2], [5,0],[1,1],[3,7], [4,4]]
ll1.sort(key=lambda x:(-x[0], x[1]))

print(" ll1 sorted -> ", ll1)


nums = [[0, 1], [1,2], [4, 0], [1,4]]
nums.sort(key=lambda x:(x[0], -x[1]))

print(" nums -> ", nums)

nums1 = [[1,2], [7,8], [3,5]]
nums1.sort(key=lambda x:-x[1])
print(" nums1 -> ", nums1)

nums2 = [[1,2], [7,8], [3,5]]
nums2.sort(reverse=True)

print(" nums2 -> ", nums2)