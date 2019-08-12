# https://medium.com/algorithms-and-leetcode/solving-matrix-graph-problems-on-leetcode-using-python-48d27fd74548
from typing import List
from collections import defaultdict
import heapq


'''
  :param n: number of cities
  :param flights: List of flights in format [src, dst, price]
  :param src: starting point
  :param dst: destination
  :param K: Number of stops
  :return: CheapestPrice (int)
  '''


class Solution:

    # https: // leetcode.com / problems / cheapest - flights - within - k - stops / discuss / 345386 / Python - Dijkstra
    def findCheapestPrice_lc(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:

        dajacencyList = defaultdict(list)
        for source, dest, price in flights:
            dajacencyList[source].append([price, dest])

        print(dajacencyList)
        minHeap = [[0, src, 0]]  # List[List[price, src, stops]]

        while minHeap:
            price, dep, stops = heapq.heappop(minHeap)
            if dep == dst:
                return price
            if stops > K:
                continue
            for nxtPrice, nxtDes in dajacencyList[dep]:
                heapq.heappush(minHeap, [price + nxtPrice, nxtDes, stops + 1])

        return -1

        print(dajacencyList)
        minHeap = [[0,src,0]] # List[List[price, src, stops]]

        while minHeap:
            price, dep, stops = heapq.heappop(minHeap)
            if dep == dst:
                return price
            if stops > K:
                continue
            for nxtPrice, nxtDes in dajacencyList[dep]:
                heapq.heappush(minHeap, [price+nxtPrice, nxtDes, stops+1])

        return -1









sol = Solution()

flights = [[0,1,100],[1,2,100],[0,2,500]]
noOfEdges = 3
src = 0
dst = 1
noOfStops = 1

cheapestPrice = sol.findCheapestPrice_lc(noOfEdges, flights, src, dst, noOfStops)
print(" cheapestPrice is -> ", cheapestPrice)