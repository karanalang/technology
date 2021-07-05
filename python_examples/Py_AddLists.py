
# afterAppend = l1.append(l2)
# print(" afterApopend -> ", afterAppend)
l1 = [1, 2, 3]
l2 = [2, 6, 7]

res = [1]
res.append(l1)
res.append(l2)

print(" res -> ", res)

print("l1.extend(l2) -> ", l1.extend(l2))

print(" l1 + l2 -> ", l1+l2)
print(type(res.append(l1)))
print(l1.extend(l2))

all = [1,2,5,7]
idx = 1
left1 = list(all[:(idx)])
right1 = list(all[(idx+1):])
print(" left -> ",left1, " right -> ", right1)
# print(left+right)
print(" left.extend(right) -> ", (left1.append(right1)))
all2 = left1.extend(right1)
print(" all2 ", all2)
