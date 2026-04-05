class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        cur_min = cur_max = nums[0]
        res = nums[0]
        for i in range(1, n):
            t1 = cur_min * nums[i]
            t2 = cur_max * nums[i]
            cur_min = min(t1, t2, nums[i])
            cur_max = max(t1, t2, nums[i])
            res = max(res, cur_min, cur_max)
            print(f'{i} {nums[i]} {t1} {t2} {cur_min} {cur_max} {res}')
        
        return res
