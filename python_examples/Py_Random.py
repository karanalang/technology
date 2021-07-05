import random

l = [1, 2, 3, 4, 5]
for i in range(5):
    print(" random from list -> ", random.choice(l))


s = {1, 2, 3, 4, 5}
for i in range(5):
    print(" random from set -> ", random.choice(tuple(s)))


# hm = {1:2, 2:3, 3:4, 4:5}
# for i in range(5):
#     print(" random from hashmap -> ", random.choice(hm))


l1 = [1, 2, 3]
l2 = [5, 6, 7, 9, 0, 10, 20, 30, 50]

seq = (l1, l2)

# print(" seq -> ", seq)
# for i in range(100):
#     c = random.choices(seq,weights=map(max(seq)-min(seq), seq))
#     print(" c -> ", c)

for i in range(5):
    print(" random.random() -> ", random.random())

for i in range(5):
    print(" randint(1,5) -> ", random.randint(1,5))

for i in range(5):
    print(" random.sample i.e. choose multiple items - no replacement -> ", random.sample([1,2,3,4,5],2))


for i in range(5):
    print(" random.choices i.e. choose multiple k items   -> ", random.choices([1,2,3,4,5, 6, 100],k=3))


print(" Choose items with probability .. weights=()")
# https://pynative.com/python-weighted-random-choices-with-probability/
input = [10, 20, 30, 40]
for i in range(10):
    print(" random.choices based on weights -> ", random.choices(input, weights=[1,10, 9, 2], k=1))


input = [10, 20, 30, 40]
for i in range(10):
    print(" random.choices based on cum_weights -> ", random.choices(input, cum_weights=[1,11, 20, 22], k=2))

# ------------
print("python accumulate")
