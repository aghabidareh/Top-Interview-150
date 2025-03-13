class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1: return 0
        if k > n / 2:
            res = 0
            for i in range(1, n):
                res += max(0, prices[i] - prices[i - 1])
            return res
        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n)]

        for i in range(n):
            for j in range(1, k + 1):
                if i == 0:
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[i]
                    continue
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
        return dp[n - 1][k][0]
