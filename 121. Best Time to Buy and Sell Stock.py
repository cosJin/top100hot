class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0 or len(prices)==1:return 0
        mini = float("inf")
        profit = 0
        for p in prices:
            profit = max(profit,p-mini)
            mini = min(p,mini)
        return profit
a = Solution()
print(a.maxProfit([7,1,5,3,6,4]))