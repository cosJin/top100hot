class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        for i in range(len(nums)):
            self.dfs(nums[i],nums[:i]+nums[i:])
    def dfs(self,pre,re):
        if re == []:
            self.res.append(pre)
            return
        else:
            for i in range(len(re)):
                self.dfs(pre+[re[i]],re[:i]+re[i:]))

