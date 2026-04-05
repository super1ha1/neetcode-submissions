class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [0] * n
        dp[0] = 1
        for i in range(n):
            if dp[i]:
                j = 0
                while j <= nums[i] and i + j < n:
                    dp[i + j] = 1
                    j += 1
                
        
        return dp[n - 1] > 0


