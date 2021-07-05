arrOfArrays = [[1, 2], [1,3], [3, 1], [3, 0, 1.1, 0], [2,7]]

sortedArr = sorted(arrOfArrays)
sortedReverse = sorted(arrOfArrays, reverse=True)

print(" sorted Array of Arrays -> ", sortedArr)
print(" sorted in reverse -> ", sortedReverse)

tup = ("1", "2", "4")
sortedTup = sorted(tup, reverse=True)
print("sortedTuple -> ", sortedTup)