# https://pypi.org/project/binarytree/
from binarytree import tree, bst, heap

my_tree_perfect = tree(height=3, is_perfect=True)
print(my_tree_perfect)

my_tree_notperfect = tree(height=3, is_perfect=False)
print(my_tree_notperfect)

my_bst_perfect = bst(height=3,is_perfect=True)
print(my_bst_perfect)


my_bst_notperfect = bst(height=3,is_perfect=False)
print(my_bst_notperfect)

my_heap_ismax_perfect = heap(height=3, is_max=True, is_perfect=True)

print(my_heap_ismax_perfect)

my_heap_isNotMax_perfect = heap(height=3, is_max=False, is_perfect=True)

print(my_heap_isNotMax_perfect)

