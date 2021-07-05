from math import *
# https://www.geeksforgeeks.org/eval-in-python/

class Python_eval:

    def usingEval(self, str):
        res = eval(str)
        print(" res -> ", res)

    def secret_function(self):
        return "Secret key is 1234"

    def function_creator(self):

        expr = input("Enter function in terms of x : ")
        x = int(input(" enter val of x : "))
        y = eval(expr) # evaluting the expression

        # printing evaluated result
        print(" y = {}".format(y))

    def function_creator_safe(self):

        safe_list = ['acos', 'asin', 'atan', 'atan2', 'ceil', 'cos',
                 'cosh', 'degrees', 'e', 'exp', 'fabs', 'floor',
                 'fmod', 'frexp', 'hypot', 'ldexp', 'log', 'log10',
                 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt',
                 'tan', 'tanh']
        safe_dict = dict([(k, locals().get(k, None)) for k in safe_list])

        print(" safe_dict -> ", safe_dict)

        # safe_dict1 = {k:None for k in safe_list}
        # print(" safe_dict1 -> ", safe_dict1)

        expr = input("Enter function in terms of x : ")
        x = int(input(" enter val of x : "))

        safe_dict['x'] = x

        y = eval(expr, {"__builtins__":None}, safe_dict) # evaluting the expression

        # printing evaluated result
        print(" y = {}".format(y))


sol = Python_eval()
str = '2*4+5'
str1 = '5/2'
# sol.usingEval(str1)
# sol.function_creator()
sol.function_creator_safe()

