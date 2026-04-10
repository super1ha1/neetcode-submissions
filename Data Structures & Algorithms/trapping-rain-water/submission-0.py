class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        for i in range(1, n - 1):
            # find left
            left = max(height[:i])
            right = max(height[i + 1:])           
            cur = min(left, right) - height[i]
            print(i, left, right, cur) 
            
            if cur > 0:
                res += cur
        
        return res
            