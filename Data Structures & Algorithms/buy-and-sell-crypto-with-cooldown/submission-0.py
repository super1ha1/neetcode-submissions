class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[0][n-1] => dp[i][j]
        # dp[i] =
        n = len(prices)
        dp = defaultdict(int)

        def dfs(i, canBuy):
            if i >= n:
                return 0
            
            if (i, canBuy) in dp:
                return dp[(i, canBuy)]
            
            do_nothing = dfs(i + 1, canBuy)

            if canBuy:
                # buy current
                buy = dfs(i + 1, not canBuy) -  prices[i]
                dp[(i, canBuy)] = max(do_nothing, buy)
            else:
                # sell current
                sell = dfs(i + 2, not canBuy) +  prices[i]
                dp[(i, canBuy)] = max(do_nothing, sell)

            return dp[(i, canBuy)]
        
        return dfs(0, True)
        
        

