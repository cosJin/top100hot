import copy
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #首先想到的是深度搜索
        self.result = []
        self.dfs(candidates,[],target)
        return self.result
    def dfs(self, candidates, res, target):
        if(target == 0): 
            # res_temp=[]
            # res_temp=res.copy()
            # 用copy()或者[:]都是给result append一个内容，其地址独立于res;
            # 若是仅仅result.append(res),那么result里面的内容仅是一个指向res的指针，其内容随res的改变而改变。
            self.result.append(res[:])
            return
        elif(target < 0): 
            return
        for n,i in enumerate(candidates):
            res.append(i)
            self.dfs(candidates[n:],res,target-i)
            res.pop()
a = Solution()
print(a.combinationSum([2,3,5],8))
