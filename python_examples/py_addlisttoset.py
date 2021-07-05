# https://stackoverflow.com/questions/1306631/add-list-to-set

s = set()

s.add(())

print(s)

for i in s:
    print(i)

# if s.__contains__(()):
print(" s contains () -> ", (), s.__contains__(()))

print(" s contains 3 -> ", s.__contains__(3))