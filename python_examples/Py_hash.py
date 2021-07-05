# https://www.programiz.com/python-programming/methods/built-in/hash
# hash function

l = [12, 6, 8, 9, 18]
a = 196.33
t = ("1", "2", "str")

print("hash of decimal -> ", hash(a))
print(" hash of string -> ", hash("Python")," - hash of string1 -> " ,hash("KaranAlang"), "- hash of tuple -> ", hash(t))

i = 201

print("hash of integer -> ", hash(i))

# hash() internally calls __hash__()
