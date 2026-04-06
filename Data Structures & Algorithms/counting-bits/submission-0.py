class Solution:
    def countBits(self, n: int) -> List[int]:
        def count(n):
            res = 0
            while n:
                if n & 1:
                    res += 1
                n = n >> 1
            
            return res
        
        res = [count(i) for i in range(n + 1)]
        return res