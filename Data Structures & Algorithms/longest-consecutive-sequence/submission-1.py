class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = set(nums)
        res = 0

        for n in nums:
            if n - 1 not in m:
                len = 1
                while n + len in m:
                    len += 1
                
                res = max(res, len)
        
        return res