class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #首先想到的DP，但是好像不太好弄呀
        #后来考虑用栈，匹配到一个字符就弹出去，最后看栈是否为空即可
        m = len(s)
        n = len(p)
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[-1][-1] = 1   #为了覆盖空字符串越界的情况，可以先设置dp[-1][-1] = 1,也不影响最终结果。
        for i in range(m):
            for j in range(n):
                if (s[i] == p[j] or p[j] == ".") and dp[i-1][j-1]==1:
                    dp[i][j] = 1
                elif p[j] == "*" and dp[i-1][j-1] == 1 and s[i] == s[i-1]:
                    dp[i][j] = 1
                elif p[j] == "*" and  dp[i][j-1] == 1:
                    dp[i][j] = 1
                else:dp[i][j] = 0
        print(dp)
        return dp[m-1][n-1]
a = Solution()
print(a.isMatch("ddf","dd**f"))

