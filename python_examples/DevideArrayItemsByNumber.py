arr = [2, 7, 9, 8]
divisor = 2

for num in arr:
    print(num//divisor)


arr = [i//divisor for i in arr]
print(" arr is -> ", arr)