class Python_PrivateMethod:

    def __init__(self, s1=""):
        self.name = s1

    def NotPrivate(self, s:str):
        print(" Hello, {}".format(s))
        self.__myPrivateMethod(s)

    def __myPrivateMethod(self, s:str):
        print(" Hello from _myPrivateMethod -> {}".format(s))




pp = Python_PrivateMethod()
pp.NotPrivate("Karan")

# shows all private & public methods
print(dir(pp))



