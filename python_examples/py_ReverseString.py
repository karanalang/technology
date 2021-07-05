class Py_ReverseString:

    def reverseString(self, s:str):

        tmp = ''
        for i in range(len(s)-1, -1, -1):
            # tmp += s[i]
            tmp += tmp.join(s[i])

        print(" reversed string -> ", tmp)



rs = Py_ReverseString()
s = 'hello'
rs.reverseString(s)
