class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # tag = False
        # print(s)
        # if len(s) == 0:return True
        # for w in wordDict:
        #     if len(s)>=len(w) and s[:len(w)] == w:
        #         tag = self.wordBreak(s[len(w):],wordDict)
        #         if tag == True: return True
        #         elif tag == False:continue
        # return False
        #动态规划，把通过字典能走到的位置置一，每到一位就检索前面为一的位到当前位能否从字典中找到。
        wordDict = set(wordDict)
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(len(s)+1)[1:]:
            for j in range(0,i+1):
                if dp[j] == 1:
                    if s[j:i] in wordDict:
                        dp[i] = 1
                        break 
        return True if dp[-1] == 1 else False


a = Solution()
s = "cars"
wordDict = ["car","ca","rs"]
print(a.wordBreak(s,wordDict))
        