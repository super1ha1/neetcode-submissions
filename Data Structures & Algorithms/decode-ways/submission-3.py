class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = {n: 1}

        def bt(i):
            if i in dp:
                return dp[i]
            if s[i] == '0':
                return 0
            
            dp[i] = bt(i + 1)

            if i < n - 1 and 10 <= int(s[i:i+2]) <= 26:
                dp[i] += bt(i + 2)
            
            return dp[i]
        
        return bt(0)
