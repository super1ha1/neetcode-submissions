class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        res = nums[0]
        cur_max = nums[0]
        for i in range(1, n):
            cur_max = max(cur_max + nums[i], nums[i])
            res = max(cur_max, res)
        
        return res

        