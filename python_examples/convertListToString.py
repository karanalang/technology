l = [1, 2, 3, 4, 5]

s = "".join([str(i) for i in l])
print(" s -> ", s)

s1 = "".join(map(str, l))

print(" s1 -> ", s1)