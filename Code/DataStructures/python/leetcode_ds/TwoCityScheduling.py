from typing import List

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        a = sorted(costs, key=lambda x : x[0] - x[1])
        print(a)
        Sa = 0
        Sb = 0
        for i in range(len(a)//2):
            Sa += a[i][0]

        for i in range(len(a) // 2, len(a)):
            Sb += a[i][1]


        return Sa + Sb



    def twoCitySchedule1(self, costs: List[List[int]]) -> int :
        ret, sub=0,[]
        for i in costs:
            ret+=i[1]
            sub.append(i[1] - i[0])
        sub.sort(reverse=True)

        print("sub -> ", sub, " ret -> ", ret)
        print(" sub[:len(costs)//2] -> ", sub[:len(costs)//2])

        return ret-sum(sub[:len(costs)//2])






s = Solution()

cost = [[10,20],[30,200],[400,50],[30,20]]
leastCost = s.twoCitySchedCost(cost)

print(" leastCost => ", leastCost)

leastCost1 = s.twoCitySchedule1(cost)
print("leastCost1 => ", leastCost1)


