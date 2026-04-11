class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            mid = l + (r - l) // 2
            
            cur = 0
            for i in piles:
                if i % mid == 0:
                    cur += i // mid
                else:
                    cur += i // mid  + 1
            
            if cur <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return res
        

        