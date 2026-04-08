class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n + 1)]

        def dfs(index, total):
            if index == n:
                if total == target:
                    return 1
                else:
                    return 0

            if dp[index].get(total, -1) != -1:
                return dp[index][total]
            
            
            dp[index][total] = dfs(index + 1, total - nums[index]) + dfs(index + 1, total + nums[index])

            return dp[index][total]
        
        return dfs(0, 0)
