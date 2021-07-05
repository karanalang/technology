from copy import copy, deepcopy

class Copy2DArray:

    def copy2DArray_deepcopy(self, board):

        res = deepcopy(board)
        print(res)

        board[0][0] = -1
        print(" board -> ", board)

        print(" res - after making cahnges to board ", res)

    def copy2DArray_copy(self, board):

        res = copy(board)
        print(" res, after copy -> ", res)

        board[0][0] = -1
        print(" board -> ", board)
        print(" res - after making cahnges to board .. res changes since it is not a deepcopy  ", res)

    def copy2DArray_map(self, board):

        res = list(map(list, board))
        print(" res -> ", res)

sol = Copy2DArray()
board = [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]

# sol.copy2DArray_deepcopy(board)
# sol.copy2DArray_copy(board)
sol.copy2DArray_map(board)