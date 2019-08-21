class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1 for _ in range(n+1)]
        for i in range(n+1)[2:]:
            dp[i] = dp[i-2] + dp[i-1]
        return dp[-1]
a = Solution()
print(a.climbStairs(3))


