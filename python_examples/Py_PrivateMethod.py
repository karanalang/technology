class Base:

    def publicMethod(self):
        return self.__privateMethod()

    # method starting  with __ (double Underscored) is a Private method
    # not accessible outside the class incl. derived class
    def __privateMethod(self):
        return "from Private Method"

# derived from Base class
class Derived(Base):

    def __init__(self):
        Base.__init__(self)

    def fromDerivedClass(self):
        # print(" from DerivedClass")
        print(" self.publicMethod -> ", self.publicMethod())

    def callingBasePrivate(self):
        print(" callingBasePrivate -> ",self.__privateMethod())
        # print(self.publicMethod())





sol = Derived()
print(sol.callingBasePrivate())