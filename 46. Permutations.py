class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        self.dfs([],nums)
        return self.res

    def dfs(self,pre,re):
        if re == []:
            self.res.append(pre)
            return
        else:
            for i in range(len(re)):
                self.dfs(pre+[re[i]],re[:i]+re[i+1:])
a = Solution()
print(a.permute([1,2,3]))
            