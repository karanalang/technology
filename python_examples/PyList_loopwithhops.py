l = [0, 0, 0, 1, 1, 1]

print(l)

# for i in range(1, len(l)+1, 2):
#     print(" i -> ",i)


for i in range(len(l)):
    print(" i -> ", i)
    for j in range(i, len(l)+1, 2):
        print("2. i -> ", i, " j -> ", j)
        print(l[i:j])