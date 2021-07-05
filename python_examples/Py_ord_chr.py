a = 'a'
print(" ascii -> ", ord(a), ' ascii symbol -> ', ascii(a))

b = 'b'
print(ord(b), " ord(b) - ord(a) -> gives the index of b -> ", ord('b')-ord('a'))

arr = [None]*26
arr[0] = ord('a') - ord('a')
print(arr)

print(" converting number to character using chr(97)-> ", chr(97+1))