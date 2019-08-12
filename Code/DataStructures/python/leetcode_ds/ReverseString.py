class ReverseString:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        length_ = len(s)
        print(" str is ", s, " length is => ", length_)
        for i in range(length_ // 2):
            print(i)
            s[i], s[length_ - 1 - i] = s[length_ - 1 - i], s[i]

        print(s)


    def test(self, s):
        length_ = len(s)
        print(length_/2)
        # // = equals to floor(length_/2)
        print(length_//2)



r = ReverseString()
str_ = 'hello'
r.reverseString(list(str_))

r.test(str_)

l = [(1, 2, 3, 45)]
reversed = l.reverse()
print(" type(l) -> ", type(l), reversed)

l1 = ["hello"]
print(l1)