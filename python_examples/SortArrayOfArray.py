arr = [[1,2],[3,4], [-1,0]]
arr.sort()
print(arr)

arr.sort(key=lambda x:x[1])

print(arr)