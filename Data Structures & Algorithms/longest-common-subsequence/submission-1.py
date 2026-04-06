class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[-1] * n for _ in range(m)]

        def bt(i, j):
            if i == len(text1) or j == len(text2):
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            if text1[i] == text2[j]:
                dp[i][j] = 1 + bt(i + 1, j + 1)
            
            else:
                dp[i][j] = max(bt(i + 1, j), bt(i, j + 1))
            
            return dp[i][j]
        
        return bt(0, 0)