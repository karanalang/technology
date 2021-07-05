# https://www.geeksforgeeks.org/count-set-bits-in-an-integer/

n = 21

def countSetBits(n):

    cnt = 0
    while n>0:
        cnt += (n & 1)
        n = n >> 1

    return cnt


setBits_iterative = countSetBits(n)
print(" setBits -> ", setBits_iterative)


def countSetBits_rec(n):

    if n==0:
        return 0

    return (n & 1) + countSetBits_rec(n >> 1)


setbits_rec = countSetBits_rec(n)
print("setbits1 -> ", setbits_rec)


def BrianAlgo(n):

    count =0
    while(n):
        print(" n -> ", n, " n-1 -> ", (n-1))
        n &= (n-1)
        count+=1
        print(" n -> ", n)

    return count


numOfSetBits_brian = BrianAlgo(n)
print(" numOfSetBits_brian -> ", numOfSetBits_brian)




