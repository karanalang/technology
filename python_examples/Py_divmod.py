x = 7
y = 2

q, r = divmod(x,y)
print(" q -> ", q, " r -> ", r)

print(" divmod(9,3) -> ", divmod(9,3))


print(" 1.divmod with float -> ", divmod(10.0,3))

print(" 2.divmod with float -> ", divmod(7.5,2.5))

print(" 3.divmod with float -> ", divmod(2.6,0.5))

def checkPrime(n):

    x = n-1
    while x >1:
        quotient, rem = divmod(n, x)
        if rem == 0:
            return False
        x -=1

    return True


print(" 5 isPrime -> ", checkPrime(5))
print(" 4 isPrime -> ", checkPrime(4))
print(" 729 isPrime -> ", checkPrime(729))

print(" 17 isPrime -> ", checkPrime(17))

def sumOfNumbers(n):

    sum = 0
    while n > 0:
        q, rem = divmod(n, 10)
        sum += rem
        n = q
    return sum


print(" 116, sum -> ", sumOfNumbers(116))
print(" 86, sum -> ", sumOfNumbers(86))


def reverseNum_1(n):
    rev = 0
    while n > 0:
        rev = rev*10 + n%10
        n //= 10

    return rev


print(" rev of 132 -> ", reverseNum_1(132))
print(" rev of 14 -> ", reverseNum_1(14))


def reverseNum_divmod(n):
    rev = 0
    while n > 0:
        q, r = divmod(n, 10)
        rev = rev*10 + r
        n = q
    return rev


print(" rev of 132, using divmod -> ", reverseNum_divmod(132))
print(" rev of 14, using divmod -> ", reverseNum_divmod(14))