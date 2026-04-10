class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        for i in range(len(nums) - k + 1):
            cur = nums[i: i + k]
            res.append(max(cur))
        
        return res