# https://stackoverflow.com/questions/22646463/and-boolean-vs-bitwise-why-difference-in-behavior-with-lists-vs-nump

l1 = [True, False, True, False, True]
l2 = [False, True, False, True, False]
print(" l1 and l2 -> ", (l1 and l2))

a = 2
b = 2
print((a ==2) and (b ==2))

if [False]:
    print("if False -> True")

l3 = [True]
l4 = [False]
print(" l3 and l4 -> ", l3 and l4)

l5 = [False]
l6 = [True]
print(" l5 and l6 -> ", l5 and l6)

wd = set(['leet','code'])
print(wd)

if 'le' in wd and True:
   print(" 'leet' in wd and True ")
else:
    print(" <- false -> ")
