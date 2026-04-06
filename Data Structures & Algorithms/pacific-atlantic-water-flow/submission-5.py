class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        def dfs(i, j, visit):
            visit.add((i, j))
            for dx, dy in direction:
                x = i + dx
                y = j + dy
                if (
                    0 <= x < m 
                and 0 <= y < n 
                and heights[x][y] >= heights[i][j]
                and ((x, y) not in visit)
                ):
                    dfs(x, y, visit)

        pa = set()
        at = set()
        for i in range(m):
            dfs(i, 0, pa)
            dfs(i, n - 1, at)
        
        for j in range(n):
            dfs(0, j, pa)
            dfs(m - 1, j, at)

        return list(pa & at)