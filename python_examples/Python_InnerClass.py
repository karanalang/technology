class Python_InnerMethod:


    def outerMethod(self):

        inouterArr = [1, 2, 3]
        res1 = 0

        def innerMethod():
            print(" In inner method, print Array declared before innerMethod ", inouterArr, " res -> ", res1)
            print(" res1 -> ", res1)
            # res1 += 1

        innerMethod()

    def outer2(self):

        res = 0
        def inner2():
            print(" res -> ", res)

        inner2()




sol = Python_InnerMethod()
sol.outerMethod()
sol.outer2()



