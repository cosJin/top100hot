class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        #方法一：动态规划
        #############
class Solution(object):
    def longestValidParentheses(self, s):

        if not s:
            return 0

        s = ' ' + s
        l = len(s)
        dp = [0] * l

        res = 0
        for i in range(1, l): #dp[n]表示从前面到n，最长的合法长度。
            if s[i] == ')' and s[i - dp[i - 1] - 1] == '(':  #表示 （ 上一串合法 ） or 上一串合法 （） 的情况  
                dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2] #表示匹配好括号的范围后，加上括号前一个的长度。
                res = max(res, dp[i])

        return res
        ############下面这个动态规划是自己写的,用的二维动态规划 （（））（（））的情况会有问题，我的就没加上一个子串的长度。因为是二维的，所以不太好加
        length = len(s)
        res = 0
        dp = [[False for _ in range(length)] for _ in range(length)]
        for n in range(0,length-1):
            if s[n] == "(" and s[n+1] == ")":
                dp[n][n+1] = True
        for i in range(length-4,-1,-1):
            print(i)
            for j in range(i+3,length):
                print("j",j)
                dp[i][j] = (dp[i+1][j-1]==1 and s[i] == "(" and s[j] == ")") or (dp[i][j-2]==1 and s[j-1] == "(" and s[j] == ")") or (dp[i+2][j]==1 and s[i] == "(" and s[i+1] == ")")
        print(dp)
        for i in range(length):
            for j in range(length):
                if dp[i][j] == True:
                    res = max(j-i+1,res)
        return res

        #方法二：栈
        class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack, longest = [0], 0
        for pos, c in enumerate(s):
            if c == '(':   
                stack.append(pos + 1)   ####之前自己想的栈的方法是压入“）”或者“（”，导致丢失位置信息，
                                        ###他的方法，压入位置信息就很好。
            elif stack.pop() > 0:
                longest = max(longest, pos + 1 - abs(stack[-1]))
            else:
                stack.append(-pos - 1)
        return longest  
a = Solution()
print(a.longestValidParentheses("(())(())"))
