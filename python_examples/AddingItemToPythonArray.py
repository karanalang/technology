nums = []
nums.append(2)

# print(nums)

arr = [1, 2, 3]
path = []

for i in range(len(arr)):
    # print(" path -> ", path)
    path = path + [arr[i]]
    print(" after adding -> ", [arr[i]],  '  path -> ', path)


p1 = []

p1 = p1 + [1]
p1 = p1 + [2]
p1 = p1 + [3]
print(p1)