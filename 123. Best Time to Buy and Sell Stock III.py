class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        num = 2
        dp = [[[0 for _ in range(len(prices))] for _ in range(2)] for _ in range(3)]  # dp[0][i] 没有股票   dp[1][i]表示有股票  情况下最大收益
        dp[2][0][0] = 0
        dp[2][1][0] = -prices[0]
        num = 2
        for i in range(len(prices))[1:]:
            if num > 0 and dp[num][1][i-1] + prices[i] > dp[num][0][i-1]:
                dp[num-1][0][i] = dp[num][1][i-1] + prices[i]
                num -= 1
            else:
                dp[num-1][0][i] = dp[num][0][i-1]

            dp[num][1][i] = max(dp[num][0][i-1] - prices[i],dp[num][1][i-1])
        print(dp)
        return max(dp[:][-1])
a = Solution()
print(a.maxProfit([3,3,5,0,0,3,1,4]))