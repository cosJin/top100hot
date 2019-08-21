class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        #状态的定义：dp[i][j] 表示word1的前i个字母 到word2的前j个字母之间的最短编辑距离
        #状态转换方程：从dp[i-1][j] dp[i][j-1] dp[i][j]之中找关系。
        n = len(word1)
        m = len(word2)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for i in range(n):
            dp[i+1][0] = i+1
        for j in range(m):
            dp[0][j+1] = j+1
        for i in range(n):
            for j in range(m):
                if word1[i] == word2[j]:dp[i+1][j+1] = dp[i][j]
                else:dp[i+1][j+1] = min(dp[i+1][j],dp[i][j+1],dp[i][j]) + 1
        return dp[-1][-1]
a = Solution()
print(a.minDistance("abc","ac"))
