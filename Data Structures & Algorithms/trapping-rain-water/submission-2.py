class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0

        l = 0
        r = n - 1
        left = height[l]
        right = height[r]

        while l < r:
            if left < right:
                l += 1
                left = max(left, height[l])
                res += left - height[l]
            else:
                r -= 1
                right = max(right, height[r])
                res += right - height[r]
        return res
            