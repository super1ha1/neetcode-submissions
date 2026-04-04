class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        n = len(s)
        start_index = 0
        resLen = 0
        
        dp = [[0] * n for _ in range(n)]
        # dp[i][j] == 1 if s[i] == s[j] and dp[i + 1][j - 1]
        for i in range(n -1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1] == 1):
                    dp[i][j] = 1
                    if j - i + 1 > resLen:
                        resLen = j - i + 1
                        start_index = i
        
        return s[start_index: start_index + resLen]