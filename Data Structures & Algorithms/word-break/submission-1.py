class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = {-1: True}

        def bt(i):
            if i in dp:
                return dp[i]

            if i < 0 or i > n:
                return False
            
            for j in range(i, -1, -1):
                if s[j:i + 1] in wordDict and bt(j - 1):
                    dp[i] = True
                    return dp[i]

            dp[i] = False
            return dp[i]
        
        return bt(n - 1)
