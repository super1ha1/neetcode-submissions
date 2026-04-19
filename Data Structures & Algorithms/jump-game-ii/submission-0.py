class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [n + 1] * n

        dp[0] = 0
        for i in range(0, n):
            if dp[i] < n + 1:
                for j in range(1, nums[i] + 1):
                    if i + j >= n:
                        break
                    dp[i + j] = min(dp[i] + 1, dp[i + j])
        
        return dp[n - 1]