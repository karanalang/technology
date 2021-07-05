# https://kite.com/python/answers/how-to-convert-a-string-to-hex-in-python#:~:text=Use%20hex()%20to%20convert,to%20convert%20it%20to%20hexadecimal.
# https://www.geeksforgeeks.org/python-hex-function/

hex_string = "1e1"
hex_int = int(hex_string, 16)

print(" hex_int -> ", hex_int)

hex_number = hex(hex_int)
print("hex_number -> ",  hex_number)

print(" string 123 is a number -> ", "123".isnumeric())

print(" string 0123 is a number -> ", "0123".isnumeric())

print(" string 0123 is a digit -> ", "0123".isdigit())

print(" hex string is numeric -> ", hex_string.isnumeric())

# "0123".isdigit()
print(" check is mixedcase ")
print("aBCd is mixed case, if not lower or upper -> ", (not "aBCd".islower() and not "aBCd".isupper()))

s = '20.1.1.100'
print(s.index('.'))
# returns valueError if value not found

print(" s.find() -> ", s.find('>'), " - ", s.find('.'))

print(ord('g')-ord('a'))

