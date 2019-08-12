
F = [0] * 50

def fibonacci_bottom_up(n):
    F[1] = 1
    F[2] = 1

    print("F -> ", F)

    for i in range(3, n+1):
        print(" i -> ", i)
        F[i] = F[i-1] + F[i-2]
    return F[n]


if __name__ == '__main__':
    fib_bottom_up = fibonacci_bottom_up(10)
    print('fib_bottom_up -> ', fib_bottom_up)



def fibonacci(n):
    if(n == 0):
        return 0
    if(n == 1):
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


fib = fibonacci(10)
print("fib -> ", fib)

# def fibonacci_dynamic(n):

FD = [-1] *50

def fibonacci_dynamic(n):

    if(FD[n] < 0):
        if(n == 1):
            FD[n] = 1
        elif (n == 2):
            FD[n] = 1
        else:
            FD[n] = fibonacci_dynamic(n-1) + fibonacci_dynamic(n-2)
    else:
        print(" FD[n] is updated -> ", FD[n])

    return FD[n]

fib_dynamic = fibonacci_dynamic(10)
print("fib_dynamic -> ", fib_dynamic)