# a = 1
# print(" a -> ", a)
#
# for i in range(32):
#     print("left shift a by 1 -> ", a << i)



n = 2

for n in range(1, 10):
    # print(" n is -> ", n ," bin n -> ", bin(n), " bin n-1 -> ", bin(n-1))
    print(" n&n-1 = 0 if n is power of 2 -> ", (n&(n-1)), " n -> ", n)


n = 2
print(" n right shift -> n/2 -> ", n>>1, " left shift n*2 -> ", 1 << n)