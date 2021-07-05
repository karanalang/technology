class Python_Map:

    def addition(self, n):
        return n + n



sol = Python_Map()
nums = [1, 2, 3, 4, 5]

print(" using map(function, iterable) ")
res = map(sol.addition, nums)
print(" map(sol.adition, nums) -> ")
print(list(res))

print(" using lambda with map i.e. map(lambda x:function, iterable) ")
res1 = map(lambda x:x*3, nums)
print(" res1 -> ", list(res1))

print(" adding 2 list using map(lambda x:x+y ")
num1 = [1,2,3]
num2 = [4,5,6]
res3 = map(lambda x,y:x+y, num1, num2)
print(" res3 -> ", list(res3))


print(" listify the list of strings individually ")
l = ['sat','bat', 'cat', 'mat']
res4 = map(list, l)
print(" res4 -> ", list(res4))