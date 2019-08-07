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
            print("target:",target,"res:",res)
            self.result.append(res)
            print("self.result:",self.result)
            return
        elif(target < 0): 
            return
        for i in candidates:
            res.append(i)
            self.dfs(candidates,res,target-i)
            res.pop()
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
            print("target:",target,"res:",res)
            self.result.append(res)
            print("self.result:",self.result)
            return
        elif(target < 0): 
            return
        for i in candidates:
            res.append(i)
            self.dfs(candidates,res,target-i)
            res.pop()
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #首先想到的是深度搜索
        result = []
        def dfs(candidates, res, target):
            if(target == 0): 
                print("target:",target,"res:",res)
                result.append(res)
                print("result:",result)
                return
            elif(target < 0): 
                return
            for i in candidates:
                res.append(i)
                self.dfs(candidates,res,target-i)
                res.pop()
        dfs(candidates,[],target)
a = Solution()
a.combinationSum2([2,3,5],8)
