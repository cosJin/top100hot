class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #自己写的只能解决aba这种奇数个回文字符串的情况，解决不了abccba的情况。
        length = maximum = 0
        res = s[0] if s != "" else ""
        for i,c in enumerate(s):
            for h in range(min(i,len(s)-i-1)):
                if s[i-h-1] == s[i+h+1]:
                    length = 2*h+3
                    if length > maximum:
                        res = s[i-h-1:i+h+2]
        return res
##########答案##########################
        #方法一：反转字符串，最长相同子字符串就是最长回文字符串。
        #       但是这种情况，会失败S = "abacdfgdcaba" S' = "abacdgfdcaba"，因为在不同位置有反向的字符串
        #       所以在找到之后要看位置是否和原位置匹配。
        #方法二：暴力法，穷举所有子字符串，看是不是回文
        #方法三：DP动态规划   状态定义：dp[i][j]表示 从 i 到 j 为回文字符串-
        #                    状态转移方程：dp[i][j] = dp[i+1][-1] if s[i] == s[j]
        #                    初始状态：dp[i][i] = 1  dp[i][i+1] = (s[i]==s[i-1])
        #方法四：围绕中心展开  */*类似于我的方法*/*  但是不仅考虑以一个节点为中心，还要考虑两个节点为中心的情况

    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        max = 0
        res = "" if s == "" else s[0]
        dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
            max = max if max > 0 else 0
            if s[i] == s[i-1] and i > 0:
                dp[i][i-1] = 1
                res = s[i-1:i+1]
                max = max if max > 1 else 1
        for j in range(len(s)):   
                 #注意一定要先循环j，这样才能逐渐找到 大一个 大一个的 回文串，
                 #否则会先遍历较长回文串的坐标，此时不能递推
            for i in range(j):
                if dp[i+1][j-1] == 1 and s[i] == s[j]:
                    dp[i][j] = 1
                    if (j - i) > max:
                        max = j - i
                        print(max,i,j)
                        res = s[i:j+1]
        return res
a = Solution()
print(a.longestPalindrome2("cbabc"))
                
