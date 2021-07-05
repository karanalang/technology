dd = {0:0, 1:1}

def fib(N):

    if N in [0,1]:
        return N

    if dd.get(N) != None:
        return dd[N]

    f1 = fib(N-1)+fib(N-2)
    dd[N] = f1
    return f1


# res = fib(998)
# print(" res -> ", res)
M = 1000000007
fact = 1

def factorial(n, fact):
    # nonlocal fact
    if n == 1:
        return 1

    res = n*factorial(n-1, fact)
    return res
n=100
# f2 = factorial(n, fact)
# print(" factorial of n == ", n , " is -> ", f2)


def factorial_usingMod(n):
    ff1 = 1

    for i in range(1, n+1):
        ff1 = (ff1*i)%M
        print(" without mod -> ", (ff1*i))

    return ff1


n = 1000
finalres = factorial_usingMod(n)
print(" final Res -> ", finalres)




