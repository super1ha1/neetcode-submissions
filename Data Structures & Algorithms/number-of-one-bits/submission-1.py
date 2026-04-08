class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        # for i in range(32):
        #     mask = 1 << i
        #     if mask & n:
        #         res += 1
        
        while n:
            if n & 1:
                res += 1
            n = n >> 1
        return res