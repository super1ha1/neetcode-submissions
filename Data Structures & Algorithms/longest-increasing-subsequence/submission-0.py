class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n

        def bt(i):
            if dp[i] != -1:
                return dp[i]
            
            lis = 1
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    lis = max(lis, 1 + bt(j))
            
            dp[i] = lis
            return dp[i]
        
        res = 1
        for i in range(n):
            res = max(res, bt(i))

        return res
