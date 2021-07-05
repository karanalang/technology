import bisect

nums = [1,2,3,4,5, 100, 300]

# bisect_left -> returns the position of insertion
pos=bisect.bisect_left(nums, 2)
print(" pos -> ",pos)

print(" nums -> ", nums)

# bisect_right -> returns the position of insertion
nums1 = [1,2,3,4,5, 100, 300]
pos1=bisect.bisect_right(nums1, 2)
print(" pos1 -> ", pos1, " nums1 -> ", nums1)

# return value - None, insort_left or right simple inserts item using binary sort
res1=bisect.insort_left(nums, 2)
print(" nums, after bisect_insort -> ", nums, " - res1 -> ", res1)

bisect.insort_right(nums, 300)
print(" nums, after bisect_insort -> ", nums)



