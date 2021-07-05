a = 5

#101
#100
#010


print(' using XOR ', (a^1))

for i in range(32):
    a=(a>>1)
    print(" a -> ", a)
    print(" a ^ 1 -> ", (a^1))