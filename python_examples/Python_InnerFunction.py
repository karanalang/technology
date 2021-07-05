# https://realpython.com/inner-functions-what-are-they-good-for/

class InnerFunction:

    def outer(self, num1):

        def inner_increment():
            # print(" num1 -> ", num1)
            return num1+2

        num2 = inner_increment()
        print(" num1 -> ", num1, " num2 -> ", num2)

sol = InnerFunction()
sol.outer(10)

