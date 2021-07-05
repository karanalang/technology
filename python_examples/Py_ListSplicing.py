l = [1, 2, 3, 4]

print(" l[:0] -> ", l[:0])

print(" l[:1] -> ", l[:1])

print(" l[1:1] -> ", l[1:1])

s = 'code'

for i in range(1, len(s)+1):
    for j in range(i):

        print(" j -> ",j, " i -> ", i ," s[j:i] -> ", s[j:i], " s[0:i] -> ", s[0:i])


