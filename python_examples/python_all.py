
print(" 1.check if all elements in list are True")
myList = [True, True, True]
print(all(myList))

print(" 2.check if all elements in list are True")
myList1 = [True, True, False]
print(all(myList1))

myList2 = [0, 0, 0]
print(all(myList2))

mydict = {1:"1", 2:'2'}
print(" all keys in dict are True -> ", all(mydict))

mydict1 = {1:"1", 2:'2', 0:"0"}
print(" all keys in dict are True -> ", all(mydict1))

print(" any elements in list is True -> ", any([True, False]))
print(" any elements is True -> ", any([False, False]))

print(" any elements is > 0 -> ", any([0, 2, 1]))

print(" any elements is True -> ", any([0, 0, 0]))

print(" any elements is True -> ", any({0:'0', 1:'1'}))



