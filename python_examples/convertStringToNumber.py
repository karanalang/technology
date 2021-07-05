# a = '1'
# print(" a[0]-0 -> ", (ord(a[0])-ord('0')))
#
# print(int('11',2))

def fun():
    a = '11'
    b = '1'
    x, y = int(a, 2), int(b, 2)
    while x:
        answer = x ^ y
        print(" answer -> ", answer)
        carry = (x & y) << 1
        print(" carry -> ", carry)
        x, y = answer, carry
        print(" x -> ", x, " y -> ", y, " bin(x)[2:] -> ", bin(x)[2:])
        return bin(x)[2:]

print(fun())