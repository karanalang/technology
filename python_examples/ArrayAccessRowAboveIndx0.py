class ArrayAccessRowAboveIdx0:

    def accessIndexMinusOne(self):

        dp = [[1,11],[2,22],[3,33]]
        # for i in dp:
        #     print(i)

        print(dp[-20], dp[0], dp[1], dp[2])

        for row in range(len(dp)):
            print(dp[row])



        # for row in range(len(dp)):
        #     for col in range(len(dp[0])):
        #         print(" row -> ", row, " col -> ", col)
        #         print(" dp[row-1][col] -> ", dp[-1][col])




sol = ArrayAccessRowAboveIdx0()
sol.accessIndexMinusOne()