class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        cur = 0
        for i in range(n):
            if cur < 0:
                return False
            elif nums[i] > cur:
                cur = nums[i]
            cur -= 1
        
        
        return True


