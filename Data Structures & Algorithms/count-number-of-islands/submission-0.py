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
            dx = [-1, 0, 1, 0]
            dy = [0, 1, 0, -1]
            for i in range(4):
                a = x + dx[i]
                b = y + dy[i]
                bt(a, b, cur)
            
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and dp[i][j] == -1:
                    res += 1
                    bt(i, j, res)
        
        return res



                
