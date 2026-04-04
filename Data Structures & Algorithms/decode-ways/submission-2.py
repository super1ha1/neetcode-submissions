class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [-1] * (n + 1)
        dp[0] = 1

        def bt(index, dp):
            if index < 0:
                return 0

            if dp[index] != -1:
                return dp[index]

            res1 = 0
            res2 = 0

            if 1 <= int(s[index - 1]) <= 9:
                res1 = 1
            try: 
                if index >= 2 and s[index - 2] != '0' and 10 <= int(s[index-2: index]) <= 26:
                    res2 = 1
            except Exception as ex:
                print(ex)
                print(s[index-2:index])
            
            # assign dp[index]
            # dp[i] = dp[i-2] + dp[i-1]
            dp[index] = res1 * bt(index - 1, dp) + res2 * bt(index - 2, dp)

            return dp[index]
        
        bt(n, dp)

        return dp[-1]
