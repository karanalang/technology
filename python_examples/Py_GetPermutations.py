from itertools import permutations

s = '123'
all_permutations = permutations(s)
# print("all_permutations -> ", list(all_permutations))
permutations = ["".join(p) for p in all_permutations]
print(" permutations -> ", permutations)

n = 4
# l = list(str(range(1,n+1)))
# ap = permutations(range(1,n+1))
# print(" ap -> ", ap)

ap1 = permutations(range(3), 2)

def permutations_rec():
    pass