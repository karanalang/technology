# https://www.programiz.com/python-programming/global-local-nonlocal-variables
# https://www.programiz.com/python-programming/global-keyword

x = 1

def foo():
    print(" accessing global varaiable inside function x -> ", x)

def changeGlobalVariable():
    global x
    x += 1
    print(" x -> ", x)

# foo()
changeGlobalVariable()

print(" x changed in function, is it changed globally -> ", x)


y = 20
def localVariableSameAsGlobalVariable():
    y = 10
    print(" local y -> ", y)

print(" global y -> ", y)
localVariableSameAsGlobalVariable()


print(" **** nonlocal example *** ")
def outer():

    x =  'local'

    def inner():
        nonlocal x
        x = "nonlocal"
        print(" inner x : ", x)

    inner()
    print(" x in outer function -> ", x)

outer()