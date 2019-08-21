class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        dp = [[0 for _ in range(len(prices))] for _ in range(2)]  # dp[0][i] 没有股票   dp[1][i]表示有股票  情况下最大收益
        dp[0][0] = 0
        dp[1][0] = -prices[0]
        for i in range(len(prices))[1:]:
            dp[0][i] = max(dp[0][i-1] ,dp[1][i-1] + prices[i] - fee)
            dp[1][i] = max(dp[0][i-1] - prices[i],dp[1][i-1])
        return max(dp[0][-1],dp[1][-1])

a = Solution()
print(a.maxProfit([1, 3, 2, 8, 4, 9],2))
