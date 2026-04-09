class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        l = 0
        r = len(heights) - 1
        
        while l < r:
            cur = (r-l) * min(heights[l], heights[r])
            res = max(res, cur)

            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        
        return res
        