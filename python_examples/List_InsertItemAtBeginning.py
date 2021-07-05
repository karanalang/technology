class List_InsertItemAtBeginning:

    def insertAtBeginning(self, l, n):
        l.insert(0, n)
        print(" after inserting at begining of List -> ", l)


sol = List_InsertItemAtBeginning()
l = [1, 2, 3, 4, 5]
n = -1
sol.insertAtBeginning(l, n)