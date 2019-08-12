toReverse = "HELLO"

def reverseString(s):
    print(s[::-1])
    print(s[-1], s[-2], s[-len(s)])
    for a in s:
        print (" item in string is {}".format(a))
    return s[::-1]


def mutableString(s):
    convertStrToList = list(s)
    print ("".join(convertStrToList))
    print (" converting String to list {}", convertStrToList)
    for s in convertStrToList:
        print(s)


def reverseString2(s):
    for a in reversed(s):
        print("In Reversed String {}".format(a))
    return "".join(reversed(s))

revstr = reverseString(toReverse)

print ("Reversed String is {}".format(revstr))


def reversedString3(s):
    list_ = list(s)
    begin = 0
    end = len(s) -1
    while begin < end:
        tmp = list_[end]
        list_[end] = list_[begin]
        list_[begin] = tmp
        begin = begin +1
        end = end - 1
    return "".join(list_)



mutableString(toReverse)

print (reverseString2(toReverse))

print (" Using classic String reversal technique => {}".format(reversedString3(toReverse)))