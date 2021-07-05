from typing import List

class SortArrayOfArray:

    def sort(self,l:List[List[int]]):

        sortedList = list(sorted(l, key=lambda x:x[1]))
        print(sortedList)

        numRooms = 1
        for i in range(len(sortedList)-1):
            # found = False
            for j in range(i+1, len(sortedList)):
                if(sortedList[i][1] > sortedList[i+1][0]):
                    numRooms += 1
                    print(" numRooms added ", numRooms, " - ", sortedList[i][1], " - ", sortedList[i+1][0])
                    # found = True
                    break




        return numRooms


s = SortArrayOfArray()
# l = [[0,30], [5,10], [15,20]]
# l = [[7,10],[2,4]]
# l = [6,15],[6,17],[13,20]
l = [[2,11],[6,16],[11,16]]
numRooms = s.sort(l)

print(numRooms)