class Array2D:

    def print2DArray(self, row:int, col:int):

        arr2d = [[0]*row]*col
        print(arr2d)

        arr2d_1 = [[0 for i in range(row)] for j in range(col)]
        print(arr2d_1)

        for i in range(len(arr2d)):
            arr2d[i][i] = 1

        print(" arr2d, set i==j to 1", arr2d)

        for i in range(len(arr2d_1)):
            arr2d_1[i][i] = 1

        print(" arr2d_1, set i==j to 1", arr2d_1)

s = Array2D()
s.print2DArray(2, 2)