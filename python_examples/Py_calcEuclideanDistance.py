from typing import List
import math

class Py_EuclideanDiatance:

    def calcEuclideanDiatnec(self, p1:List[int], p2:List[int]):

        d1 = math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
        print(" d1 -> ", d1)

        d2 = math.sqrt(sum((a-b)**2 for a, b in zip(p1, p2)))

        print(" d2 -> ", d2)
        print(" d1 == d2 -> ", (d1 == d2))

        pass



ed = Py_EuclideanDiatance()
p1 = [2, 2]
p2 = [0, 0]
ed.calcEuclideanDiatnec(p1, p2)