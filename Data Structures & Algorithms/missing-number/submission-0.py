class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        m = set(nums)
        for i in range(n):
            if i not in m:
                return i
        return None