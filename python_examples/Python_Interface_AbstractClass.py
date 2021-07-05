import abc

class py_interface:

    testmethod = None

    @abc.abstractmethod
    def method1(self, metaclass=abc.ABCMeta):
        pass

    def method2(self):
        pass