# https://www.geeksforgeeks.org/random-numbers-in-python/
import random
print(" get 1 random number from list", random.choice([4, 100, 3, 2, 7, 8]))

print(" get 1 random number between 2 numbers -> ", random.randrange(20, 50))
print(" get 1 random number between 2 numbers, with skip step  -> ", random.randrange(20, 50, 3))

print(" random number between 0 and 1 -> ", random.random())

print("using seed() to seed different random number")
print(" randon.seed -> ", random.seed(7))

print(" mapped random number with seed = 7 ", random.random())

random.seed(5)
for i in range(10):
    random.seed(5)
    print(" mapped number with seed = 5 -> ", random.random())

print(" generating random integers usig randint", random.randint(4, 100))


l = [1, 6, 97, 0.5]
print(" using shuffle. list Before shuffle ", l)
random.shuffle(l)

print(" after shuffle(l) -> ", l)


print(" using uniform() , to get floaing number between 5 and 10 -> ", random.uniform(5, 10))

for i in range(10):
    print(random.randint(0, 9))

# randint vs randrange