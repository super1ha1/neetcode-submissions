class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # total = sum(nums)
        # if total % 2 == 1:
        #     return False
        # target = total // 2
        # n = len(nums)
        # dp = [[-1] * target for _ in range(n)]

        # def bt(index, cur_sum):
        #     if cur_sum == target:
        #         return True
        #     if index == n - 1 or cur_sum > target:
        #         return False
            
        #     if dp[index][cur_sum] != -1:
        #         return dp[index][cur_sum]

        #     dp[index][cur_sum] =  bt(index + 1, cur_sum) or bt(index + 1, cur_sum + nums[index])
               
        #     return dp[index][cur_sum]
        
        # return bt(0, 0)

        if sum(nums) % 2:
            return False

        target = sum(nums) // 2
        dp = [False] * (target + 1)

        dp[0] = True
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[target]