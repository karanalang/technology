# https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_singleton.htm

class PythonSingleton:

    __instance = None

    '''
    In python, the constructor cannot be made Private *like in Java
    Hence, constructor 
    '''
    def __init__(self):
        if PythonSingleton.__instance:
            raise Exception(' This is Python Singleton ')
        else:
            PythonSingleton.__instance = self


    @staticmethod
    def getInstance(self):
        '''
        Static method, returns Singleton object if present,
        else creates
        :param self:
        :return:
        '''
        if not PythonSingleton.__instance:
            PythonSingleton()

        return PythonSingleton.__instance





singleton = PythonSingleton()
singleton2 = PythonSingleton.getInstance(singleton)
singleton1 = PythonSingleton.getInstance(singleton)

print(singleton == singleton1)
print(singleton1 == singleton2)
print(singleton == singleton2)
