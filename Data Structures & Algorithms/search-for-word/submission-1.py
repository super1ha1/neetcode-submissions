class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        visit = set()
        direction = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        def bt(i, j, index):
            if index == len(word):
                # success
                return True
            
            for dx, dy in direction:
                x = i + dx
                y = j + dy
                if 0 <= x < m and 0 <= y < n and board[x][y] == word[index] and (x, y) not in visit:
                    visit.add((x, y))
                    if bt(x, y, index + 1):
                        return True
                    visit.remove((x, y))
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visit.add((i, j))
                    if bt(i, j, 1):
                        return True
                    visit.remove((i, j))
        
        return False
        

