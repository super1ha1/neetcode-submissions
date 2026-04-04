class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        
        dp = [0] * n
        # 2 scenario
        # rob house 1
        dp[0] = nums[0]
        dp[1] = dp[0]

        for i in range(2, n - 1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        cur_max = dp[n-2]

        # do not rob house 1
        dp[0] = 0
        dp[1] = nums[1]
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        return max(cur_max, dp[n - 1])
        


        