from TreeNode import TreeNode
from typing import List
from collections import deque

class Solution:
    def spriralOrderTraversal(self, root:TreeNode) -> List[List[int]]:

         odd_ = deque()
         even_ = deque()
         spriralOrderTraversalList = []


         if(root):
             odd_.append(root)

         while(len(odd_) != 0 or len(even_) !=0):

             print(" odd_ len ", len(odd_), " even len ", len(even_))

             while(len(odd_) != 0):

                currOddList = []

                sizeOdd = len(odd_)
                for i in range(sizeOdd):
                    i = odd_.popleft()
                    print(" popleft from odd_ ", i.val)
                    currOddList.append(i.val)

                    if(i.left):
                        print("1. adding to even -> ", i.left.val)
                        even_.append(i.left)
                    if(i.right):
                        print(" 2.adding to even -> ", i.right.val)
                        even_.append(i.right)

                    for i in range(len(even_)):
                        print("1.even_ after adding items, index -> ", i, " <- item -> ", even_[i].val)

                print(" 1. adding to spriralOrderTraversalList, currOddList ", currOddList)
                spriralOrderTraversalList.append(currOddList)

             while (len(even_) != 0):

                currEvenList = []
                sizeEven = len(even_)
                for i in range(sizeEven):
                    i = even_.pop       ()
                    print(" pop from even List -> ", i.val)
                    currEvenList.append(i.val)

                    if (i.left):
                        print("1.adding to Odd_ ", i.left.val)
                        odd_.append(i.left)
                    if(i.right):
                        print("2.adding to Odd_ ", i.right.val)
                        odd_.append(i.right)

                    for i in range(len(odd_)):
                        print("1.odd_ after adding items, index -> ", i, " <-item -> ", odd_[i].val)


                print(" 2. adding to spriralOrderTraversalList, currEvenList ", currEvenList)
                spriralOrderTraversalList.append(currEvenList)


         return spriralOrderTraversalList



    def zigzagOrderTraversal(self, root:TreeNode) -> List[List[int]]:
        """
        :param root:
        :return:
        """
        queue, level = [root],1
        res = []
        if(not root):
            return res


        while(queue):
            if(level%2 !=0):
                res.append([node.val for node in queue])
            else:
                res.append([node.val for node in queue][::-1])

            pairs = [(node.left, node.right) for node in queue]
            queue = [leaf for lr in pairs for leaf in lr if leaf]

            level += 1

        return res




root = TreeNode(3)
l11 = TreeNode(9)
l12 = TreeNode(20)
l21 = TreeNode(15)
l22 = TreeNode(7)

root.left = l11
root.right = l12
l12.left = l21
l12.right = l22

# [1,2,3,4,null,null,5]

root_1 = TreeNode(1)
l1_1 = TreeNode(2)
l1_2 = TreeNode(3)
l2_1 = TreeNode(4)
l2_2 = TreeNode(5)

root_1.left = l1_1
root_1.right = l1_2
l1_1.left = l2_1
l1_2.right = l2_2

s = Solution()
t = s.spriralOrderTraversal(root_1)
print(" t -> ", t)

s.zigzagOrderTraversal()

# expected -> [[1],[3,2],[4,5]]