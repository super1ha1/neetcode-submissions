import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        num = []
        for p1, p2 in points:
            distance = math.sqrt(p1*p1 + p2*p2)
            num.append([distance, p1, p2])

        heapq.heapify(num)
        # filter k smallest distance
        res = []
        for i in range(k):
            distance, x, y = heapq.heappop(num)
            res.append([x, y])
        
        return res