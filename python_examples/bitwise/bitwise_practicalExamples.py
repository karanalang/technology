print(" check if number is power of 2")

N = 8
print(" binary version of N -> ", bin(N)[2:])
print(" binary version of N-1 -> ", bin(N-1)[2:])

print(" if N & (N-1), then N is power of 2 ", (N&(N-1)))


print(" Find single integer in sorted array that appears twice")
l  = [1,2,3,3,100, 7]

for i in range(1, len(l)):
    print(l[i]^l[i-1])
    if (l[i]^l[i-1] == 0):
        print(" duplicate number -> ", l[i])


print(" Find single integer in array that DOES NOT appear Twice")
# why this works -> XOR returns 1 only if elements are different, so if elements are same, result = 0

l1 = [1, 1, 2, 2, 3, 3, 6]
sum1 = 0
for i in range(len(l1)):
    sum1 ^= l1[i]
    print(" sum1 -> ", sum1)

print(" sum1 i.e. integer that DOES NOT APPEAR TWICE -> ", sum1)

print(" SWAP numbers without using a temporary variable i.e. using XOR ")

x = 5
y = 7
x = x^y
y = x^y
x = x^y
print(" x -> ", x, " y -> ", y)


print(" multiply by 2, using left shift ")
print(" rightshift 2 times ie (15>>1)>>1 -> ", 15>>2, " - right shift 2 times -> ", (15>>1)>>1)
print(7>>1)

print(" left shift 1 times ie (5<<1)<<1 -> ", 5<<1, " - left shift 2 times -> ", (5<<1)<<1)




