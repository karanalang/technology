from typing import List
from collections import OrderedDict
from collections import UserDict
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Py_verticalOrderTraversal:

    # def __init__(self):
    #     dq = deque()
    #     dict_ = {}  # hashtable

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:

        dq = deque()
        dict_ = {}  # hashtable
        verticalTraversalList = []

        if(root):
            dq.append(root)
            # dict_[100000] = ([root.val])
            dict_[0] = ([root.val])

        verticalTraversalList.append(dict_[0])

        print(' verticalTraversalList -> ', verticalTraversalList)

        print("dict_ with root -> ", dict_)

        d = self.doVerticalTraversal(root, 0, dq, dict_)
        print('final dict -> ', d)

        return None



    def doVerticalTraversal(self, root, hk, dq, dict_):

        while (len(dq) != 0):
            size_ = len(dq)

            for i in range(size_):
                i = dq.popleft()

                if (i.left):
                    dq.append(i.left.val)
                    # updating the dict fotr key -> (hk -1)
                    hk_left = hk -1
                    print(" hk_left -> ", hk_left)
                    dict_[hk_left].append(i.left.val)

                if (i.right):
                    dq.append(i.right.val)
                    hk_right = hk+1
                    print(" hk_right -> ", hk_right)
                    dict_[hk_right].append(i.right.val)

            self.doVerticalTraversal(i.left, hk_left), dq, dict_
            self.doVerticalTraversal(i.left, hk_right, dq, dict_)


        return dict










root = TreeNode(3)
l11 = TreeNode(9)
l12 = TreeNode(20)
l21 = TreeNode(15)
l22 = TreeNode(7)

root.left = l11
root.right = l12
l12.left = l21
l12.right = l22


s = Py_verticalOrderTraversal()
s.verticalTraversal(root)