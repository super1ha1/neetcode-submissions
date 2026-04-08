class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        n = len(coins)
        dp = [[-1] *  (n + 1) for _ in range(amount + 1)]

        def dfs(index, total):
            if total == 0:
                return 1
            if index >= len(coins):
                return 0

            if dp[total][index] != -1:
                return dp[total][index]

            res = 0
            if total >= coins[index]:
                res += dfs(index + 1, total)
                res += dfs(index, total - coins[index])
            dp[total][index] = res
            return dp[total][index]
        return dfs(0, amount)