# https://python-reference.readthedocs.io/en/latest/docs/functions/unichr.html
# https://www.geeksforgeeks.org/ord-function-python/
# https://www.geeksforgeeks.org/python-ways-to-convert-list-of-ascii-value-to-string/

class Py_ord:

    def usingOrd(self):
        print(ord('A'), ord('a'), ord("$"), ord("B"))
        print(ord("A")-ord("0"))

        try:
            print(ord("$"), ord('65'))
        except:
            print(" convert to Unicode ord expects single charater, not a string")

        print(ord('a'), ord('b'), ord('c'), ord('d'), ord('e'), ord('f'), ord('g'))

    def usingChr(self):
        print(" opposite of ord(A) <chr(int val of unicode charater A) -> ", chr(65), " of character a -> ", chr(97))
        print(" opposite of ord($), chr(<int val of uicode character $>) -> ", chr(36))

    def convertToAcscii(self):
        print(" get ascii value -> ", chr(65), " convert to Ascii (1) -> ", ascii(1))




sol = Py_ord()
sol.usingOrd()
sol.usingChr()
sol.convertToAcscii()