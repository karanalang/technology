# https://www.programiz.com/python-programming/examples/ascii-character

class Py_AsciiValues:

    def getAsciiValues(self, s):
        print(' asciivalue of ', s, " is -> ", ord(s), type(ord(s)))


    def getCharFromAscii(self, ascii):

        print(' ascii  -> ', ascii, ' string -> ', chr(ascii))
        pass


s = Py_AsciiValues()
s1 = 'leetcode'
s.getAsciiValues('A')
s.getCharFromAscii(65)