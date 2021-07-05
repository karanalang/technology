arr = [1, 2, 3]

for i in range(len(arr)):
    tmpArr = []
    for j in range(i+1, len(arr)):
        # print(" subArray -> ", arr[i:j])
        print(" all combinations -> ", [arr[i]]+[arr[j]])