d = {'a':2, 'b':1, 'c':3}

print(" using sorted, key=lambda x:x[1] .. gives  a list of (key, val)-> ", sorted(d.items(), key=lambda x:x[1]))

dsorted = sorted(d.items(), key=lambda x:x[1])
print(type(sorted(d.items(), key=lambda x:x[1])))


print(" using sorted, key=d.get .. gives only the keys as an array -> ", sorted(d, key=d.get))

print(type(sorted(d, key=d.get)))