num = 2

# cntOfSetBits = 0
# for i in range(1, 32):
#     # global cntOfSetBits
#     print(" Before right shift i times -> ", num)
#     num = (num>>i)
#     print(" after right shift i times -> ", num)
#     if num&1 == 1:
#         print(" setbit found ")
#         cntOfSetBits+=1
#
# print(" cntOfSetits -> ", cntOfSetBits)

cntOfSetBits_1 = 0
for i in range(31, -1, -1):
    # global cntOfSetBits
    print(" Before right shift i times -> ", num)
    num1 = (num<<i)
    print(" after right shift i times -> ", num)
    if num1&1 == 1:
        print(" setbit found ")
        cntOfSetBits_1+=1