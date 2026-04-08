class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        num = [-x for x in stones]
        heapq.heapify(num)

        while len(num) >= 2:
            p1 = -heapq.heappop(num)
            p2 = -heapq.heappop(num)
            p3 = p1 - p2
            if p3 == 0:
                continue
            else:
                heapq.heappush(num, -p3)
        
        if len(num) == 0:
            return 0
        return -num[0]

