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
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0] = 1   #0 表示空字符串
        if n >=2 and p[1] == "*": 
            dp[0][2] = 1
            j = 3
            while j<=n:
                if p[j-1] == "*": 
                    dp[0][j] = 1
                    j+=1
                else:break
                
        for i in range(1,m+1):
            for j in range(1,n+1):
                if (s[i-1] == p[j-1] or p[j-1] == ".") and dp[i-1][j-1]==1:
                    dp[i][j] = 1
                elif p[j-1] == "*" and dp[i-1][j-1] == 1 and s[i-1] == s[i-2]:
                    dp[i][j] = 1
                elif p[j-1] == "*" and  dp[i][j-1] == 1:  #这个一开始没考虑到
                    dp[i][j] = 1
                elif (p[j-1] == "*" and p[j-2] == "." and dp[i-2][j] == 1):
                    dp[i][j] = 1
        return dp[-1][-1]
a = Solution()
print(a.isMatch("aab","c*a*b"))

