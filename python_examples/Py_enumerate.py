# https://www.afternerd.com/blog/python-enumerate/

class UsingEnumerate:

    def usingEnumerateList(self, l):
        print(" using enumerate ")
        e = enumerate(l)
        print(" type(e) -> ", e)
        for index, val in enumerate(l):
            print(" index -> ", index, " val -> ", val)

    def enumerateTuple(self, t):
        e = enumerate(t)
        for index, (name, age) in e:
            print(" index -> ", index, " name -> ", name, " age -> ", age)


    def enumerateStr(self, s1, start):

        for index, ch in enumerate(s1):
            print(" Enumerate w/o start : index -> ", index, " ch -> ", ch)

        for index, ch in enumerate(s1, start=start):
            print(" Enumerate WITH StartIndex : index -> ", index, " ch -> ", ch)


s = UsingEnumerate()
l = ['a', 'b', 'c']
s.usingEnumerateList(l)
t=[("k1", 10), ("k2", "21")]
s.enumerateTuple(t)

s1 = "Python"
s.enumerateStr(s1, 2)