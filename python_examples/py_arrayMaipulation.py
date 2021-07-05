arr = [1,2,4]
arr_deepcopy = arr.copy()
print(" arr_deepcopy -> ", arr_deepcopy)

arr.append(6)
print(" arr -> ", arr, " arr_deepcopy -> ", arr_deepcopy)


# append to tmpPath, and simultaneously add to Path

paths = []
n = 5
def appendToPaths():

    def rec(node, tmpPath):
        if node == n:
            tmpPath.append(node)
            paths.append(tmpPath.copy())
            return

        # tmpPath + node
        tmpPath.append(node)
        # print(" tmpPath.append(node) ", tmpPath.append(node), tmpPath+[node])
        rec(node+1, tmpPath)


    rec(0,[])
    return paths

res = appendToPaths()
print(" paths -> ", paths)







