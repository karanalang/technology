from typing import List

class GenerateAllDistances:

    def genAllDistances(self, p1: List[int], p2:List[int], p3:List[int], p4:List[int]):

        pts = [p1, p2, p3, p4]
        distances = []

        for i in range(4):
            for j in range(i+1, 4):
                dist = self.getDistance(pts[i], pts[j])
                distances.append(dist)

        # distances = sorted(distances)
        # print(" distances -> ", distances)

    def checkSquare(self, distances):

        s1, s2, s3, s4, d1, d2 = 0



    def getDistance(self, p1, p2) -> int:

        return (p1[0] - p2[0])** 2 + (p1[1] - p2[1])**2



s = GenerateAllDistances()
p1 = [0,0]
p2 = [1,1]
p3 = [1,0]
p4 = [0,1]
s.genAllDistances(p1, p2, p3, p4)