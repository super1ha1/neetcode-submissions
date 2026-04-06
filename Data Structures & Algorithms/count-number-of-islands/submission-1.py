class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[-1] * n for _ in range(m)]

        def bt(x, y, cur):
            if x < 0 or x >= m or y < 0 or y >= n:
                return
            
            if dp[x][y] != -1: 
                return
            
            # label current
            if grid[x][y] == '0':
                dp[x][y] = 0
                return

            dp[x][y] = 1

            direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
            for dx, dy in direction:
                bt(x+dx, y + dy, cur)
            
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and dp[i][j] == -1:
                    res += 1
                    bt(i, j, res)
        
        return res



                
