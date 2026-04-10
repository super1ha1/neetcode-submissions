class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0

        # left max
        left = [0] * n
        right = [0] * n
        left[0] = height[0]
        for i in range(1, n):
            left[i] = max(left[i-1], height[i])
        
        right[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], height[i])

        for i in range(1, n - 1):
            # find left
            l = left[i]
            r = right[i]      
            cur = min(l, r) - height[i]
            print(i, l, r, cur) 
            
            if cur > 0:
                res += cur
        
        return res
            